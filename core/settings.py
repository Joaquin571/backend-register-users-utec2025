import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env") 

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

#DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.postgresql',
   #     'NAME': os.getenv('DB_NAME'),
    #    'USER': os.getenv('DB_USER'),
     #   'PASSWORD': os.getenv('DB_PASSWORD'),
      #  'HOST': os.getenv('DB_HOST'),
       # 'PORT': os.getenv('DB_PORT', '5432'),
 #   }
#}


SECRET_KEY = os.getenv("SECRET_KEY") 

STATIC_URL = "static/"              
STATIC_ROOT = BASE_DIR / "staticfiles"

DEBUG = True
ALLOWED_HOSTS = ["*"]  

INSTALLED_APPS = [
    "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes",
    "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles",
    "rest_framework", "corsheaders",
    "users",
]

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


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "DEFAULT_PARSER_CLASSES": ["rest_framework.parsers.JSONParser"],
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOW_ALL_ORIGINS = True  

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8080", 
    "http://localhost:8080",
    "http://127.0.0.1:5500", 
    "http://localhost:5500",

]

NOTIF_BASE_URL = os.getenv(
    "NOTIF_BASE_URL",
    "http://notification-service:8081", 
).rstrip("/")

NOTIF_FROM_EMAIL = os.getenv("NOTIF_FROM_EMAIL", "")

NOTIFICATION_SERVICE_URL = os.getenv(
    "NOTIFICATION_SERVICE_URL",
    f"{NOTIF_BASE_URL}/notify/email/welcome",
)
