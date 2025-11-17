import json
import logging
import os

from sqlalchemy import func

from app import db
from app.config.country_config import country_config
from app.models._geo_region import GeoRegion

GEOMETRIES_DATA_DIR = './app/_static_data/geometries'
REGIONS_GEOJSON_FILE = 'bfa_regions.geojson'

def load_regions():
    logging.info("[GEOMETRIES LOADING][REGIONS]: Loading regions")

    if not os.path.exists(GEOMETRIES_DATA_DIR):
        logging.error("[GEOMETRIES LOADING][REGIONS]: Geometries data directory does not exist")
        return

    config = country_config.get('BFA')

    iso = config.get("iso")

    logging.info("[GEOMETRIES LOADING][REGIONS]: Loading boundaries for {}".format('BFA'))

    geojson_file = os.path.join(GEOMETRIES_DATA_DIR, f"{iso.lower()}_regions.geojson")

    if not os.path.exists(geojson_file):
        logging.info(f"[GEOMETRIES LOADING][REGIONS]: File {geojson_file} does not exist")
        return

    logging.info(f"[GEOMETRIES LOADING][REGIONS]: Loading {geojson_file}")

    id_field = config.get("id_field")
    name_field = config.get("name_field")

    with open(geojson_file, "r") as f:
        geojson = json.load(f)

        features = geojson.get("features")

        for feature in features:
            props = feature.get("properties")

            id_prop = props.get(id_field)
            name = props.get(name_field)

            if id_prop is None and name is None:
                logging.info(f"[REGION]: Skipping ")
                continue

            gid = f"{iso}_{id_prop}"

            geom = feature.get("geometry")
            geom_type = geom.get("type")

            # convert to multipolygon
            if geom_type == "Polygon":
                geom = {
                    "type": "MultiPolygon",
                    "coordinates": [geom.get("coordinates")]
                }

                georegion_data = {
                    "gid": gid,
                    "country_iso": iso,
                    "name": name,
                    "geom": func.ST_GeomFromGeoJSON(json.dumps(geom))
                }

                db_georegion = GeoRegion.query.get(georegion_data.get("gid"))
                exists = False

                if db_georegion:
                    exists = True

                db_georegion = GeoRegion(**georegion_data)

                if exists:
                    logging.info('[REGION]: UPDATE')
                    db.session.merge(db_georegion)
                else:
                    logging.info('[REGION]: ADD')
                    db.session.add(db_georegion)

                db.session.commit()
