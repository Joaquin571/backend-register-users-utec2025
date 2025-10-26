#!/usr/bin/env bash
set -e

# Espera opcional por el service de notificaciones (no necesario para SQLite)
# sleep 1

python manage.py migrate --noinput

# Para desarrollo con hot reload, podrías usar runserver.
# En "modo contenedor" estable lanzamos gunicorn.
# (Django es WSGI; si tu proyecto fuera ASGI podrías usar uvicorn/daphne)
exec gunicorn core.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 3 \
  --threads 2 \
  --timeout 60
