from django import template
from allauth.account.utils import has_verified_email


# internals

register = template.Library()


@register.simple_tag
def get_website():
    from apps.core.models import Website

    return Website.objects.first()


@register.simple_tag
def is_email_verified(user, email):
    return has_verified_email(user, email)


@register.simple_tag
def get_themes():
    return [
        "agate",
        "atom-one-dark",
        "atom-one-light",
        "default",
        "far",
        "felipec",
        "foundation",
        "github-dark",
        "github",
        "kimbie-light",
        "mono-blue",
        "monokai-sublime",
        "night-owl",
        "purebasic",
        "qtcreator-light",
        "school-book",
        "srcery",
        "stackoverflow-dark",
        "stackoverflow-light",
        "vs",
        "vs2015",
        "xt256",
    ]
