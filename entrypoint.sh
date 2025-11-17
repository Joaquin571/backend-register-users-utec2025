#!/usr/bin/env bash
set -e


python manage.py migrate --noinput


exec gunicorn core.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3 \
  --threads 2 \
  --timeout 60
