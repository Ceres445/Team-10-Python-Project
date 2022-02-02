"""
Django settings for SchoolApp project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import dj_database_url
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "ph+0qjo^*#n_!*d=nizy4ly7$dm-&nvk9yq0&_*#(=gxgd-*-w"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY", "ph+0qjo^*#n_!*d=nizy4ly7$dm-&nvk9yq0&_*#(=gxgd-*-w"
)
# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "apps.home",
    "apps.public_api",
    "apps.classes",
    "apps.timetable",
    "rest_framework",
    "invitations",
    "storages",
    "django_simple_bulma",
    "drf_yasg",
    "django.contrib.admin",
    "django.contrib.sites",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
]

SITE_ID = 1

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

ROOT_URLCONF = "SchoolApp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
            # 'loaders': [
            #     'django.template.loaders.app_directories.Loader'
            # ]
        },
    },
]

WSGI_APPLICATION = "SchoolApp.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# database for heroku

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)

# set allowed hosts for heroku
ALLOWED_HOSTS = [
    "school-portal-ceres.herokuapp.com",
    "127.0.0.1",
    "localhost",
    "0.0.0.0",
    "edu-orange.herokuapp.com",
]


# Static files
STATIC_URL = "/static/"
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django_simple_bulma.finders.SimpleBulmaFinder",
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

if os.environ.get("HOST", None) != "heroku":
    load_dotenv()
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication"
    ],
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '100/day',
    #     'user': '1000/day'
    # }
}

# static file storage
DEFAULT_FILE_STORAGE = "storages.backends.dropbox.DropBoxStorage"
DROPBOX_OAUTH2_TOKEN = os.environ.get("DROPBOX_ACCESS_TOKEN")

# Auto fields
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# INVITATIONS app settings
INVITATIONS_SIGNUP_REDIRECT = ""
INVITATIONS_INVITATION_EXPIRY = 0
INVITATIONS_GONE_ON_ACCEPT_ERROR = False
INVITATIONS_EMAIL_SUBJECT_PREFIX = "Team10- "

# TIME ZONE
TIME_ZONE = "Asia/Kolkata"
USE_TZ = True

# Caching
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "unix:/tmp/memcached.sock",
    }
}
colors = {"orange_color": "hsl(35, 100%, 45%)"}
BULMA_SETTINGS = {
    "extensions": [
        "bulma-collapsible",
        "bulma-navbar-burger",
        "bulma-collapsible-runner",
        "bulma-fileupload",
    ],
    "variables": {
        "footer-background-color": "hsl(12,33%,9%)",
        "title-color": "white",
        "box-color": "white",
        "box-background-color": "hsl(216, 50%, 12%)",
        "table-row-hover-background-color": "hsl(34, 100%, 74%)",
        "message-header-background-color": "hsl(222, 50%, 18%)",
        "scheme-main": "hsl(36, 95%, 40%)",  # main color (orange)
        "scheme-main-bis": "hsla(0, 0, 90%, 0.11)",  # nth even color
        "scheme-main-ter": "hsl(36, 95%, 66%)",  # nth hover color
        "border": "hsl(200, 42%, 26%)",  # border color
        "link": colors["orange_color"],
        "grey-darker": "black",
        "navbar-item-hover-color": "black",
        "link-hover": "hsl(36, 95%, 66%)",
        "link-active": "black",
        "link-focus": "black",
        "text": "black",
        "text-strong": "black",
        "link-invert": "hsla(0, 0%, 100%, 0.15)",
        "background": "hsla(0, 0%, 100%, 0.15)",
        "size-1": "5rem",
    },
    "output_style": "compressed",
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(asctime)s [%(process)d] [%(levelname)s] "
                + "pathname=%(pathname)s lineno=%(lineno)s "
                + "funcname=%(funcName)s %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        # "testlogger": {
        #     "handlers": ["console"],
        #     "level": "INFO",
        # },
        "django": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
