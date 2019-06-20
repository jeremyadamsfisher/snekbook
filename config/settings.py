import os
from os import path
import django_heroku
import dj_database_url
import dotenv

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
dotenv_file = path.join(BASE_DIR, ".env")
if path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = bool(os.environ.get("DEBUG", False))
ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"]
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "widget_tweaks",
    # custom apps
    "apps.snekbook",
    "apps.accounts",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "config.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]
WSGI_APPLICATION = "config.wsgi.application"

DATABASES = None
if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "localdb",
            "USER": "localuser",
            "TEST": {"NAME": "mytestdatabase"},
        }
    }
else:
    DATABASES = {"default": dj_database_url.config(conn_max_age=600)}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS = (
    path.join(BASE_DIR, "static"),
    path.join(BASE_DIR, "data_scrubber", "thumbs"),
)

FIXTURE_DIRS = path.join(BASE_DIR, "tests", "fixtures")

django_heroku.settings(locals())
# hacky workaround to get dj_database_url to forget about SSL at the last second
if "OPTIONS" in DATABASES["default"]:
    DATABASES["default"]["OPTIONS"].pop("sslmode")
