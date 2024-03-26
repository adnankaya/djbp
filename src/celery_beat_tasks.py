####################################################################
#####                                                          #####
##### Define Production tasks here. For development use dev.py #####
#####                                                          #####
####################################################################
from celery.schedules import crontab


# Register your tasks here to be scheduled
beat_schedule = {
    "health_check_task": {
        "task": "src.tasks.health_check_task",
        "schedule": crontab(minute="*/5"),
    },
    
}
