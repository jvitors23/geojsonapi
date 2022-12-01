#!/bin/sh
echo "Running entrypoint"
python manage.py collectstatic --noinput
python manage.py migrate
echo "Starting server"
gunicorn geojsonapi.wsgi:application --config gunicorn-cfg.py
