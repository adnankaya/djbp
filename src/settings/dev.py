from .base import *
from celery.schedules import crontab



DEBUG = True

ALLOWED_HOSTS = ["*"]


CELERY_BEAT_SCHEDULE = {
    "health_check_task": {
        "task": "src.tasks.health_check_task",
        "schedule": crontab(minute="*/2"),
    },
}