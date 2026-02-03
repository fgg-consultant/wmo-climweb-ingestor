import logging
from datetime import datetime

import requests
from dateutil import parser as date_parser

from app import db
from app.config import SETTINGS
from app.models.flood_gauge import FloodGauge
from app.models.flood_status import FloodStatus

GOOGLE_FLOOD_API_BASE_URL = "https://floodforecasting.googleapis.com/v1"


def load_flood_status(country_code: str):
    """
    Fetch latest flood status from Google Flood API and upsert into database.

    Args:
        country_code: ISO 3166-1 alpha-2 country code (e.g., 'BFA' for Burkina Faso)
    """
    api_key = SETTINGS.get('GOOGLE_FLOOD_API_KEY')
    if not api_key:
        logging.error("[INGESTION][FLOOD_STATUS]: GOOGLE_FLOOD_API_KEY not configured")
        return

    logging.info(f"[INGESTION][FLOOD_STATUS]: Loading flood status for country {country_code}")

    flood_statuses = []
    request_body = {
        'regionCode': country_code,
        'pageSize': 10000,
        'includeNonQualityVerified': False,
    }

    while True:
        response = requests.post(
            f'{GOOGLE_FLOOD_API_BASE_URL}/floodStatus:searchLatestFloodStatusByArea?key={api_key}',
            json=request_body
        )

        if response.status_code != 200:
            logging.error(f"[INGESTION][FLOOD_STATUS]: API error: {response.status_code} - {response.text}")
            return

        data = response.json()

        if 'error' in data:
            logging.error(f"[INGESTION][FLOOD_STATUS]: API error: {data['error']}")
            return

        new_statuses = data.get('floodStatuses', [])
        flood_statuses.extend(new_statuses)

        next_page_token = data.get('nextPageToken')
        if not next_page_token:
            break
        request_body['pageToken'] = next_page_token

    logging.info(f"[INGESTION][FLOOD_STATUS]: Fetched {len(flood_statuses)} flood statuses from API")

    count_added = 0
    count_updated = 0
    count_skipped = 0

    for status_data in flood_statuses:
        gauge_id = status_data.get('gaugeId')
        issued_time_str = status_data.get('issuedTime')

        if not gauge_id or not issued_time_str:
            logging.warning(f"[INGESTION][FLOOD_STATUS]: Skipping status with missing data: {status_data}")
            count_skipped += 1
            continue

        # Check if gauge exists
        gauge = FloodGauge.query.filter_by(gauge_id=gauge_id).first()
        if not gauge:
            logging.warning(f"[INGESTION][FLOOD_STATUS]: Gauge {gauge_id} not found, skipping status")
            count_skipped += 1
            continue

        issued_time = date_parser.isoparse(issued_time_str)
        severity = status_data.get('severity', 'UNKNOWN')
        forecast_trend = status_data.get('forecastTrend')
        quality_verified = status_data.get('qualityVerified', False)
        source = status_data.get('source')

        # Parse forecast time range
        forecast_time_range = status_data.get('forecastTimeRange', {})
        forecast_start = None
        forecast_end = None
        if forecast_time_range.get('start'):
            forecast_start = date_parser.isoparse(forecast_time_range['start'])
        if forecast_time_range.get('end'):
            forecast_end = date_parser.isoparse(forecast_time_range['end'])

        # Parse value change
        forecast_change = status_data.get('forecastChange', {})
        value_change = forecast_change.get('valueChange', {})
        value_change_lower = value_change.get('lowerBound')
        value_change_upper = value_change.get('upperBound')

        existing = FloodStatus.query.filter_by(
            gauge_id=gauge_id,
            issued_time=issued_time
        ).first()

        if existing:
            existing.severity = severity
            existing.forecast_trend = forecast_trend
            existing.quality_verified = quality_verified
            existing.source = source
            existing.forecast_start = forecast_start
            existing.forecast_end = forecast_end
            existing.value_change_lower = value_change_lower
            existing.value_change_upper = value_change_upper
            count_updated += 1
        else:
            new_status = FloodStatus(
                gauge_id=gauge_id,
                issued_time=issued_time,
                severity=severity,
                forecast_trend=forecast_trend,
                quality_verified=quality_verified,
                source=source,
                forecast_start=forecast_start,
                forecast_end=forecast_end,
                value_change_lower=value_change_lower,
                value_change_upper=value_change_upper
            )
            db.session.add(new_status)
            count_added += 1

    db.session.commit()
    logging.info(f"[INGESTION][FLOOD_STATUS]: Done. Added: {count_added}, Updated: {count_updated}, Skipped: {count_skipped}")
