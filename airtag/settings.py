import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY SETTINGS
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
DEBUG = os.getenv("DEBUG", "True") == "True"

# Hosts allowed to serve this app
ALLOWED_HOSTS = [
    "airsneakers-backend.onrender.com",
    "airsneakers-frontend.vercel.app",
    "127.0.0.1",
    "localhost"
]

# Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "store",
]

# Middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # CORS first
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "airtag.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "airtag.wsgi.application"

# Database
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
DATABASES = {
    "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)
}

# Password validation
AUTH_PASSWORD_VALIDATORS = []

# Localization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =====================
# CORS SETTINGS
# =====================
CORS_ALLOWED_ORIGINS = [
    "https://airsneakers-frontend.vercel.app",
    "http://localhost:3000",
    "http://localhost:5500"
]
CORS_ALLOW_ALL_ORIGINS = True if DEBUG else False

# =====================
# SSLCommerz Sandbox Settings
# =====================
SSLC_STORE_ID = os.getenv("SSLC_STORE_ID", "airsn68981bba6ded8")
SSLC_STORE_PASSWORD = os.getenv("SSLC_STORE_PASSWORD", "airsn68981bba6ded8@ssl")
SSLC_SUCCESS_URL = os.getenv("SSLC_SUCCESS_URL", "https://airsneakers-frontend.vercel.app/payment-success")
SSLC_FAIL_URL = os.getenv("SSLC_FAIL_URL", "https://airsneakers-frontend.vercel.app/payment-fail")
SSLC_CANCEL_URL = os.getenv("SSLC_CANCEL_URL", "https://airsneakers-frontend.vercel.app/payment-cancel")

# =====================
# Email (optional)
# =====================
EMAIL_BACKEND = (
    "django.core.mail.backends.smtp.EmailBackend"
    if os.getenv("EMAIL_BACKEND") == "smtp"
    else "django.core.mail.backends.console.EmailBackend"
)
EMAIL_HOST = os.getenv("EMAIL_HOST", "")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
