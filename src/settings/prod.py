from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "adnankaya.github.io localhost").split(" ")


# for secure connection use rediss://
CELERY_REDIS_BACKEND_USE_SSL = {"ssl_cert_reqs": ssl.CERT_NONE}
BROKER_USE_SSL = {"ssl_cert_reqs": ssl.CERT_NONE}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(asctime)s %(message)s"},
    },
    "handlers": {
        "db_log": {
            "level": "INFO",
            "class": "django_db_logger.db_log_handler.DatabaseLogHandler",
        },
    },
    "loggers": {
        "db": {"handlers": ["db_log"], "level": "INFO"},
        "django.request": {  # logging 500 errors to database
            "handlers": [
                "db_log",
            ],
            "level": "INFO",
            "propagate": False,
        },
    },
}
