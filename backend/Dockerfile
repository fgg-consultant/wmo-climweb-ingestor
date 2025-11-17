# pull base image
FROM python:3.11-slim

RUN apt-get update -y && apt-get install -y cron ca-certificates

RUN pip install poetry==1.6.1
RUN poetry config virtualenvs.create false

WORKDIR /code

COPY ./backend/pyproject.toml ./backend/README.md ./backend/poetry.lock* ./

RUN poetry install  --no-interaction --no-ansi --no-root

COPY ./backend/app ./app
COPY ./backend/migrations ./migrations
COPY ./.env ./.env

RUN poetry install --no-interaction --no-ansi

COPY ./backend/ingest.cron /etc/cron.d/ingest.cron
RUN chmod 0644 /etc/cron.d/ingest.cron && crontab /etc/cron.d/ingest.cron

COPY ./backend/docker-entrypoint.sh ./docker-entrypoint.sh
RUN chmod +x ./docker-entrypoint.sh
ENTRYPOINT ["/code/docker-entrypoint.sh"]

EXPOSE 8001

CMD exec gunicorn -b 0.0.0.0:8001 app:app_flask
