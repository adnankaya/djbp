import os
from django.conf import settings


def get_user_notifications(request):
    """To use user notifications globally"""
    if request.user.is_authenticated:
        LIMIT = 5
        if settings.NOTIFICATONS_CONFIG["SOFT_DELETE"]:
            qset = request.user.notifications.active()
        else:
            qset = request.user.notifications.all()
        return {"user_notifications": qset[:LIMIT]}
    return []


def google_tag_manager(request):
    return {"GTM_ID": os.getenv("GTM_ID", "None")}
