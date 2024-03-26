import os
import celery
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@celery.shared_task
def health_check_task():
    logger.info(
        f"health_check_task() is running. DJANGO_SETTINGS_MODULE is {os.getenv('DJANGO_SETTINGS_MODULE')}"
    )
