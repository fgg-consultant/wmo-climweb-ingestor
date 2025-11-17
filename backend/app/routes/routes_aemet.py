import logging
from datetime import timedelta

from flask import jsonify
from sqlalchemy import desc

from app.models.dustforecast import DustForecast
from app.models.dustwarning import DustWarning
from app.routes import endpoints


@endpoints.route('/dustwarning/forecast_dates', strict_slashes=False, methods=['GET'])
def get_available_dates():
    logging.info('[ROUTER][DUST_WARNING]: Getting available dates')

    dates = []

    latest_init_date = DustWarning.query.order_by(desc(DustWarning.init_date)).first()

    if latest_init_date:
        latest_init_date = latest_init_date.init_date
        dates.append(latest_init_date)

        # add next two days
        for i in range(1, 3):
            dates.append(latest_init_date + timedelta(days=i))

    dates = [date.strftime("%Y-%m-%dT%H:%M:%S.000Z") for date in dates]

    response = {
        "timestamps": dates
    }

    return jsonify(response), 200

@endpoints.route('/dustforecast/forecast_dates', strict_slashes=False, methods=['GET'])
def get_dustforecast_available_dates():
    logging.info('[ROUTER][DUST_FORECAST]: Getting available 3-hourly dust forecast timestamps (fixed 0..72h from today 00:00 UTC)')

    timestamps = []
    latest_init_date = DustForecast.query.order_by(desc(DustForecast.init_date)).first()

    if latest_init_date:
        latest_init_date = latest_init_date.init_date
        base_dt = latest_init_date.replace(hour=0, minute=0, second=0, microsecond=0)
        timestamps = [ (base_dt + timedelta(hours=i*3)).strftime("%Y-%m-%dT%H:%M:%S.000Z") for i in range(25) ]

    return jsonify({"timestamps": timestamps}), 200
