import logging

from flask import jsonify
from sqlalchemy import desc

from app import db
from app.models.flood_gauge import FloodGauge
from app.models.flood_status import FloodStatus
from app.routes import endpoints


@endpoints.route('/floodstatus/issued_dates', strict_slashes=False, methods=['GET'])
def get_flood_status_issued_dates():
    """Return available issued timestamps for flood status data."""
    logging.info('[ROUTER][FLOOD_STATUS]: Getting available issued dates')

    dates = db.session.query(
        FloodStatus.issued_time
    ).distinct().order_by(desc(FloodStatus.issued_time)).all()

    timestamps = [d[0].strftime("%Y-%m-%dT%H:%M:%S.000Z") for d in dates if d[0]]

    return jsonify({"timestamps": timestamps}), 200


@endpoints.route('/floodstatus/gauges', strict_slashes=False, methods=['GET'])
def get_flood_gauges():
    """Return all flood gauges with their latest status."""
    logging.info('[ROUTER][FLOOD_STATUS]: Getting flood gauges with latest status')

    # Subquery to get latest status per gauge
    latest_status_subq = db.session.query(
        FloodStatus.gauge_id,
        db.func.max(FloodStatus.issued_time).label('max_issued_time')
    ).group_by(FloodStatus.gauge_id).subquery()

    # Join gauges with their latest status
    results = db.session.query(FloodGauge, FloodStatus).outerjoin(
        latest_status_subq,
        FloodGauge.gauge_id == latest_status_subq.c.gauge_id
    ).outerjoin(
        FloodStatus,
        db.and_(
            FloodStatus.gauge_id == latest_status_subq.c.gauge_id,
            FloodStatus.issued_time == latest_status_subq.c.max_issued_time
        )
    ).all()

    gauges = []
    for gauge, status in results:
        gauge_data = gauge.serialize()
        if status:
            gauge_data['latest_status'] = status.serialize()
        else:
            gauge_data['latest_status'] = None
        gauges.append(gauge_data)

    return jsonify({"gauges": gauges}), 200
