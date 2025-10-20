
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")  # <- carga variables del .env

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


SECRET_KEY = os.getenv("SECRET_KEY")  # <- ahora sí existe

# --- ⚙️ ESTÁTICOS (mínimo para DEV) ---
STATIC_URL = "static/"               # <- esto es lo que te falta
# Opcional (útil para prod/collectstatic):
STATIC_ROOT = BASE_DIR / "staticfiles"

DEBUG = True
ALLOWED_HOSTS = ["*"]  # solo DEV

INSTALLED_APPS = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles",
    "rest_framework", "corsheaders",
    "users",
]
# Archivo de URLs raíz del proyecto
ROOT_URLCONF = "core.urls"

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],            
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# DRF sólo JSON
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
}

# Email por consola (para la captura del Ej.1)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Recomendado por Django 3.2+
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- CORS (solo desarrollo) ---
CORS_ALLOW_ALL_ORIGINS = True   # permite llamadas desde cualquier origen en dev

# Si servís el front con Live Server u otro puerto, agregalo acá:
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
]
