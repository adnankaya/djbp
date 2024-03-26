from django import forms

from apps.core.models import Waitlist


class SearchForm(forms.Form):
    query = forms.CharField()


class WaitlistForm(forms.ModelForm):
    class Meta:
        model = Waitlist
        fields = ("email",)
