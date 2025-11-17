import logging
import os
import re

import click
from sqlalchemy.sql import text

from app import db
from app.ingest.aemet.ingestor_dustforecast import load_forecast
from app.ingest.aemet.ingestor_dustwarning import load_warnings
from app.ingest.geometries.geometries_loader import load_regions


########################
# SETUP DB COMMANDS
########################
@click.command(name="setup_schema")
def setup_schema():
    logging.info("[DBSETUP]: Setting up schema")
    schema_sql = f"""DO
                $do$
                BEGIN
                    CREATE EXTENSION IF NOT EXISTS postgis;
                    CREATE SCHEMA IF NOT EXISTS aemet;
                END
                $do$;"""
    
    db.session.execute(text(schema_sql))
    db.session.commit()
    
    logging.info("[DBSETUP]: Done Setting up schema")

@click.command(name="create_pg_functions")
def create_pg_functions():
    logging.info("[DBSETUP]: Creating pg functions")

    # Run all sql scripts in app/_db/ folder
    sql_files_directory = './app/_db/'
    for filename in os.listdir(sql_files_directory):
        if re.search(r'\.sql$', filename):
            sql_file_path = os.path.join(sql_files_directory, filename)
            try:
                with open(sql_file_path, 'r') as file:
                    sql_script = file.read()
                    db.session.execute(text(sql_script))
                    db.session.commit()
                    logging.info(f"[DBSETUP]: Executed SQL script from {sql_file_path}")
            except Exception as e:
                logging.error(f"[DBSETUP]: Error executing {sql_file_path}: {e}")
    logging.info("[DBSETUP]: Done Creating pg function")

########################
# INGESTION COMMANDS
########################
@click.command(name="load_geometries")
def load_geometries():
    load_regions()

@click.command(name="ingest_dustwarning")
def ingest_dustwarning():
    logging.info("[INGESTION][DUST_WARNINGS]: Start")
    load_warnings()

@click.command(name="ingest_dustforecast")
def ingest_dustforecast():
    logging.info("[INGESTION][DUST_FORECAST]: Start")
    load_forecast()

