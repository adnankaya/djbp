import uuid
import random
from decimal import Decimal
from django.db import models
from django.db.models import Sum, Avg, Prefetch, Count, Q, F
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from apps.core.models import BaseModel, BaseUuidModel


class User(AbstractUser):

    class Meta:
        db_table = "t_user"

    def __str__(self) -> str:
        return self.email or self.username

    def get_full_name(self) -> str:
        fullname = super().get_full_name()
        if not fullname:
            return self.username
        return fullname

    @classmethod
    def get_system_user(cls):
        return cls.objects.get(username="system-user")


class UserSocialAddress(BaseModel):

    class Type(models.TextChoices):
        instagram = "instagram", _("instagram")
        tiktok = "tiktok", _("tiktok")
        twitter = "twitter", _("twitter")
        facebook = "facebook", _("facebook")
        linkedin = "linkedin", _("linkedin")

    url = models.URLField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    social_type = models.CharField(max_length=32, choices=Type.choices)

    class Meta:
        db_table = "t_user_social_address"

    def __str__(self) -> str:
        return self.url


class Profile(BaseUuidModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=32, null=True, blank=True)
    job = models.CharField(max_length=64, null=True, blank=True)
    title = models.CharField(max_length=64, null=True, blank=True)
    country = models.CharField(max_length=64, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    timezone = models.CharField(max_length=64, default="UTC")

    class Meta:
        abstract = True


class Client(Profile):

    class Meta:
        db_table = "t_client"

    def get_absolute_url(self):
        return reverse("users:clients-detail", args=(self.id,))
