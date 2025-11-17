#!/bin/sh

echo "Setup Schema"
flask --app=app setup_schema

echo "Running Migrations"
flask --app=app db upgrade

echo "Create PG Functions"
flask --app=app create_pg_functions

echo "Load geometries"
flask --app=app load_geometries

# ensure cron is running
service cron start
service cron status

exec "$@"
