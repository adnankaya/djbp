from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.db import transaction


from allauth.account.views import EmailView
from allauth.account.models import EmailAddress

from .models import Client


@login_required()
def me_profile(request):
    context = {"title": _("My Profile Page")}

    return render(request, "users/me-profile.html", context)


class UserEmailView(EmailView):
    success_url = reverse_lazy("users:emails")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "emailaddresses" in context:
            del context["emailaddress_radios"]
            context["emailaddresses"] = EmailAddress.objects.filter(
                user=self.request.user
            ).order_by("email")
        return context

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@login_required
def update(request):
    """
    Authenticated user info update
    """
    ctx = {}
    pass

@login_required
def clients_detail(request, cid: str):
    client = get_object_or_404(Client, id=cid)
    is_owner = False

    if request.user.client == client:
        is_owner = True

    context = {
        "title": "Client Detail",
        "client": client,
        "is_owner": is_owner,
    }
    return render(request, "users/clients/detail.html", context)
