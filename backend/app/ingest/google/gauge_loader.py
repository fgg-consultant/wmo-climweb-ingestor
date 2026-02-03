import logging

import requests
from shapely.geometry import Point
from geoalchemy2.shape import from_shape

from app import db
from app.config import SETTINGS
from app.models.flood_gauge import FloodGauge

GOOGLE_FLOOD_API_BASE_URL = "https://floodforecasting.googleapis.com/v1"


def load_gauges(country_code: str):
    """
    Fetch gauges from Google Flood API and upsert into database.

    Args:
        country_code: ISO 3166-1 alpha-2 country code (e.g., 'BFA' for Burkina Faso)
    """
    api_key = SETTINGS.get('GOOGLE_FLOOD_API_KEY')
    if not api_key:
        logging.error("[INGESTION][FLOOD_GAUGES]: GOOGLE_FLOOD_API_KEY not configured")
        return

    logging.info(f"[INGESTION][FLOOD_GAUGES]: Loading gauges for country {country_code}")

    gauges = []
    request_body = {
        'regionCode': country_code,
        'pageSize': 10000,
    }

    while True:
        response = requests.post(
            f'{GOOGLE_FLOOD_API_BASE_URL}/gauges:searchGaugesByArea?key={api_key}',
            json=request_body
        )

        if response.status_code != 200:
            logging.error(f"[INGESTION][FLOOD_GAUGES]: API error: {response.status_code} - {response.text}")
            return

        data = response.json()

        if 'error' in data:
            logging.error(f"[INGESTION][FLOOD_GAUGES]: API error: {data['error']}")
            return

        new_gauges = data.get('gauges', [])
        gauges.extend(new_gauges)

        next_page_token = data.get('nextPageToken')
        if not next_page_token:
            break
        request_body['pageToken'] = next_page_token

    logging.info(f"[INGESTION][FLOOD_GAUGES]: Fetched {len(gauges)} gauges from API")

    count_added = 0
    count_updated = 0

    for gauge_data in gauges:
        gauge_id = gauge_data.get('gaugeId')
        location = gauge_data.get('location', {})
        latitude = location.get('latitude')
        longitude = location.get('longitude')

        if not gauge_id or latitude is None or longitude is None:
            logging.warning(f"[INGESTION][FLOOD_GAUGES]: Skipping gauge with missing data: {gauge_data}")
            continue

        point = Point(longitude, latitude)
        geom = from_shape(point, srid=4326)

        existing = FloodGauge.query.filter_by(gauge_id=gauge_id).first()

        if existing:
            existing.site_name = gauge_data.get('siteName')
            existing.river = gauge_data.get('river')
            existing.country_code = gauge_data.get('countryCode', country_code)
            existing.source = gauge_data.get('source')
            existing.quality_verified = gauge_data.get('qualityVerified', False)
            existing.has_model = gauge_data.get('hasModel', False)
            existing.geom = geom
            count_updated += 1
        else:
            new_gauge = FloodGauge(
                gauge_id=gauge_id,
                site_name=gauge_data.get('siteName'),
                river=gauge_data.get('river'),
                country_code=gauge_data.get('countryCode', country_code),
                source=gauge_data.get('source'),
                quality_verified=gauge_data.get('qualityVerified', False),
                has_model=gauge_data.get('hasModel', False),
                geom=geom
            )
            db.session.add(new_gauge)
            count_added += 1

    db.session.commit()
    logging.info(f"[INGESTION][FLOOD_GAUGES]: Done. Added: {count_added}, Updated: {count_updated}")
