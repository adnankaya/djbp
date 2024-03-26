from django.contrib import admin

# Register your models here.
from apps.core.models import Waitlist, Website

admin.site.register(Waitlist)
admin.site.register(Website)