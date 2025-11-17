import json
import logging
from datetime import datetime, timedelta

import pytz
from sqlalchemy import func

from app import db
from app.models.dustforecast import DustForecast
from app.utils import get_json_warnings


def load_forecast():

    # 25 timestamps: 0h to 72h ahead every 3 hours => indices 00..24
    hour_indices = [f"{i:02d}" for i in range(25)]

    next_update = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    target_timezone = pytz.timezone('Europe/Paris')
    current_time_utc_plus_one = datetime.now(target_timezone)

    # only run after 12:05 UTC+1 (when upstream data likely ready)
    if current_time_utc_plus_one < current_time_utc_plus_one.replace(hour=12, minute=5):
        logging.warning(f"[DUST_FORECAST]: Skipping forecasts update as it is before 12:05 UTC+1. Current time is {current_time_utc_plus_one}")
        return None

    if not next_update:
        return None

    next_update_str = next_update.strftime("%Y%m%d")

    # Skip if already ingested for this init_date
    existing_data = DustForecast.query.filter_by(init_date=next_update).first()
    if existing_data:
        logging.info(f"[INGESTION][DUST_FORECAST]: Data for date {next_update_str} already exists. Skipping.")
        return None

    logging.info("[INGESTION][DUST_FORECAST]: Loading 3-hourly forecasts (0..72h) for init {}".format(next_update_str))

    # URL template uses index (00..24) in filename
    geojson_url_template = "https://dust.aemet.es/daily_dashboard/assets/geojsons/median/geojson/{date_str}/{index}_{date_str}_SCONC_DUST.geojson"

    forecast_batches = []  # collect all records then bulk add

    for idx in hour_indices:
        # Convert index to hour offset (index * 3 hours)
        forecast_datetime = next_update + timedelta(hours=int(idx) * 3)

        geojson_url = geojson_url_template.format(date_str=next_update_str, index=idx)
        logging.info(f"[INGESTION][DUST_FORECAST]: Fetching forecast step {idx} (T+{int(idx)*3}h) -> {geojson_url}")

        try:
            geojson_forecast = get_json_warnings(geojson_url)
            if not geojson_forecast:
                logging.warning(f"[INGESTION][DUST_FORECAST]: Empty response for {geojson_url}")
                continue

            features = geojson_forecast.get("features") or []
            if not features:
                logging.warning(f"[INGESTION][DUST_FORECAST]: No features for {geojson_url}")
                continue

            for feature in features:
                props = feature.get("properties", {})
                id_prop = feature.get("id")
                if id_prop is None:
                    logging.debug(f"[DUST_FORECAST]: Skipping feature without id at step {idx}")
                    continue

                value = props.get("value")
                if value is None:
                    logging.debug(f"[DUST_FORECAST]: Missing 'value' for id {id_prop} step {idx}")
                    continue

                geom = feature.get("geometry") or {}
                geom_type = geom.get("type")
                if geom_type == "Polygon":
                    geom = {"type": "MultiPolygon", "coordinates": [geom.get("coordinates")]}  # normalize

                record = {
                    "gid": f"{id_prop}",
                    "init_date": next_update,
                    "forecast_date": forecast_datetime,
                    "value": value,
                    "geom": func.ST_GeomFromGeoJSON(json.dumps(geom))
                }
                forecast_batches.append(record)

        except Exception as e:
            logging.error(f"[INGESTION][DUST_FORECAST]: Error fetching step {idx} (T+{int(idx)*3}h): {e}")
            continue

    # Persist to DB (upsert-like behavior)
    added = 0
    updated = 0
    for record in forecast_batches:
        db_forecast = DustForecast.query.filter_by(init_date=record["init_date"],
                                                   forecast_date=record["forecast_date"],
                                                   gid=record["gid"]).first()
        if db_forecast:
            db_forecast.value = record["value"]
            updated += 1
        else:
            db_forecast = DustForecast(**record)
            db.session.add(db_forecast)
            added += 1
    if forecast_batches:
        db.session.commit()

    logging.info(f"[INGESTION][DUST_FORECAST]: Done. Added: {added}, Updated: {updated}, Total processed steps: {len(hour_indices)}")
    return None
