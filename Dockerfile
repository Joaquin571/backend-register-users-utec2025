FROM python:3.11-slim

# Evitar prompts y cache
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Sistema base (build deps + tzdata recomendado)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential tzdata curl && \
    rm -rf /var/lib/apt/lists/*

# Copiamos requirements y los instalamos
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copiamos la app
COPY . /app

# Entrypoint ejecutará migraciones y luego arranca el server
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Puerto interno (gunicorn)
EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
