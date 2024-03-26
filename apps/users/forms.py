from django import forms
from django.utils.translation import gettext as _

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = []
