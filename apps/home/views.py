from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext as _
from django_htmx.middleware import HtmxDetails
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from apps.core.forms import WaitlistForm


# Typing pattern recommended by django-stubs:
# https://github.com/typeddjango/django-stubs#how-can-i-create-a-httprequest-thats-guaranteed-to-have-an-authenticated-user
class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

##########   HTMX views  ######################################################
@require_GET
@login_required
def dashboard_chart_line(request: HtmxHttpRequest) -> HttpResponse:
    context = {}
    return render(request, "home/dashboard/partials/chart-line.html", context)


@require_GET
@login_required
def dashboard_chart_bar(request: HtmxHttpRequest) -> HttpResponse:
    context = {}
    return render(request, "home/dashboard/partials/chart-bar.html", context)


###############################################################################

def index(request):

    context = {"title": _("Home page")}

    return render(request, "home/index.html", context)


@require_GET
@login_required
def dashboard(request: HtmxHttpRequest) -> HttpResponse:
    ctx = {"title": "Dashboard"}

    return render(request, "home/dashboard/index.html", ctx)





def pricing(request):

    context = {"title": _("Pricing page")}

    return render(request, "home/pricing/index.html", context)


def contact(request):

    context = {"title": _("Contact Us Page")}

    return render(request, "home/contact/index.html", context)


def aboutus(request):

    context = {"title": _("About Us Page")}

    return render(request, "home/aboutus/index.html", context)


def faq(request):

    context = {"title": _("F.A.Q Page")}

    return render(request, "home/faq/index.html", context)


def privacy(request):

    context = {"title": _("Privacy Page")}

    return render(request, "home/privacy/index.html", context)


def terms(request):

    context = {"title": _("Terms Page")}

    return render(request, "home/terms/index.html", context)


@require_POST
def waitlist_register(request):
    form = WaitlistForm(request.POST)
    if form.is_valid():
        email = form.save()
        messages.success(
            request,
            _(
                "Thanks for joining. We look forward to notify you when platform is ready to use."
            ),
        )
    else:
        messages.error(request, form.errors)
    return HttpResponseRedirect(reverse("home:index"))
