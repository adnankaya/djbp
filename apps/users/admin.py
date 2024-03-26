from django.contrib import admin
from .models import User, Client, UserSocialAddress

# Register your models here.

admin.site.register(User)
admin.site.register(Client)
admin.site.register(UserSocialAddress)
