from pathlib import Path

from .env import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config.get("SECRET_KEY", default="j84f$-1laihz+c*o7612!qtf!^idf!8ql%x^bprhn48%^afigb")
DEBUG = config.get("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config.get("ALLOWED_HOSTS", default="*", cast=lambda v: [s.strip() for s in v.split(",")])

INSTALLED_APPS = [
    "proxy_service.apps.hacker_news",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "proxy_service.app.urls"
WSGI_APPLICATION = "proxy_service.app.wsgi.application"
USE_I18N = True
USE_TZ = True

from .components import *  # noqa: F401,E402,F403
