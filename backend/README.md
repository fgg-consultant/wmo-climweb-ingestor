# WMO Climweb Ingestor - Backend

## Development mode
### Setup the environment
- Copy `.env.sample` to `.env` and fill in the required values.
- Check you have Python 3.11 installed.
```bash
python3.11 -m venv .venv
poetry install
source .venv/bin/activate
```

### Run DB and PGTileServ as docker containers

This will open `55432` (postgres) & `7800` (pg_tilerv) ports on localhost.
```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml up
````

### Setup database and datas

```bash
flask --app=app setup_schema
flask --app=app db upgrade
flask --app=app create_pg_functions
flask --app=app load_geometries
```

### Ingestion commands

Ideally, ingestion commands should be run in a cron job or similar scheduling system. Here are some examples of how to
run them manually:

```bash
flask --app=app ingest_riverine
flask --app=app ingest_flashflood
flask --app=app update_riverine 200384 2025-05-25 2025-05-25 40
```

## Web application (backend API)

#### Development mode

`python3.11 main.py` to run the web server on port `8001`.


#### Routes

* GET http://localhost:8001/api/v1/riverineflood
* POST http://localhost:8001/api/v1/riverineflood/<subid>

```
  Content-Type: application/json
  {
    "value": 52,
    "init_date": "2025-07-01",
    "forecast_date": "2025-07-01"
  }
```

* GET http://localhost:8001/api/v1/flashflood
* POST http://localhost:8001/api/v1/flashflood/<subid>

```
  Content-Type: application/json
  {
    "value": 52,
    "forecast_date": "2025-07-01"
  }
```

