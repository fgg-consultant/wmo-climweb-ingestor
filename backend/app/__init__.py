import logging
import sys

from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from healthcheck import HealthCheck

from app.config import SETTINGS
from app.routes import endpoints

logging.basicConfig(
    level=SETTINGS.get('logging', {}).get('level'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y%m%d-%H:%M%p',
)

# Flask App
app_flask = Flask(__name__, template_folder=SETTINGS.get("TEMPLATE_DIR"))
auth = HTTPBasicAuth()
CORS(app_flask)

logger = logging.getLogger(__name__)
logger.setLevel(SETTINGS.get('logging', {}).get('level'))
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

app_flask.config['SQLALCHEMY_DATABASE_URI'] = SETTINGS.get('SQLALCHEMY_DATABASE_URI')
app_flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app_flask)
migrate = Migrate(app_flask, db)

health = HealthCheck(app_flask, "/healthcheck")


def db_available():
    db.session.execute('SELECT 1')
    return True, "dbworks"


health.add_check(db_available)

import app.routes.routes_aemet
import app.routes.routes_google
app_flask.register_blueprint(endpoints, url_prefix='/api/v1')

from app import commands

app_flask.cli.add_command(commands.setup_schema)
app_flask.cli.add_command(commands.create_pg_functions)
app_flask.cli.add_command(commands.load_geometries)
app_flask.cli.add_command(commands.ingest_dustwarning)
app_flask.cli.add_command(commands.ingest_dustforecast)
app_flask.cli.add_command(commands.load_flood_gauges_command)
app_flask.cli.add_command(commands.ingest_floodstatus_command)
