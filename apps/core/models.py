import uuid
from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    copy_exclude_fields = ["created_date", "updated_date", "pk", "id"]

    class Meta:
        abstract = True

    def copy_into(self, instance: models.Model) -> models.Model:
        """copy this object's field values into instance(target)"""
        for field in self._meta.fields:
            if not field.name in self.copy_exclude_fields:
                setattr(instance, field.name, getattr(self, field.name))
        return instance


class BaseUuidModel(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Website(BaseModel):
    name = models.CharField(max_length=60, unique=True)
    en_meta_description = models.TextField()
    en_meta_keywords = models.TextField()
    tr_meta_description = models.TextField()
    tr_meta_keywords = models.TextField()

    class Meta:
        db_table = "t_website"
        verbose_name = "Website"
        verbose_name_plural = "Websites"

    def __str__(self) -> str:
        return self.name


class Waitlist(BaseModel):
    email = models.EmailField(max_length=64, unique=True)

    class Meta:
        db_table = "t_waitlist"

    def __str__(self) -> str:
        return self.email
