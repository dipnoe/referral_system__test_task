#!/bin/bash

./manage.py migrate &&
./manage.py collectstatic --noinput &&
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --reload