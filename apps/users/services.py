from django.utils.translation import gettext as _
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.utils import timezone
from django.db.models import Q, QuerySet
from django.urls import reverse_lazy


from .tokens import get_account_activation_token


class UserService(object):
    @classmethod
    def send_email_verification(cls, user, domain):
        _template = "users/activate-user.html"
        url = reverse_lazy(
            "users:activate",
            kwargs={
                "uidb64": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": get_account_activation_token().make_token(user),
            },
        )
        activate_url = "{}{}".format(domain, url)
        _context = {
            "user": user,
            "activate_url": activate_url,
        }
        mail_subject = _("Email confirmation.")
        message = render_to_string(_template, _context)
        email = EmailMessage(
            subject=mail_subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )
        email.content_subtype = "html"
        email.send()

    @classmethod
    def send_email_for_new_user(cls, user):
        _template = "users/new-user-joined.html"

        _context = {
            "user": user,
        }
        mail_subject = _("New user joined.")
        message = render_to_string(_template, _context)
        email = EmailMessage(
            subject=mail_subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=settings.SITE_ADMINS,
        )
        email.content_subtype = "html"
        email.send()

    @classmethod
    def send_email_user_activated(cls, user):
        _template = "users/user-activated.html"
        _context = {
            "user": user,
        }
        mail_subject = _("Your account has been activated")
        message = render_to_string(_template, _context)
        email = EmailMessage(
            subject=mail_subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[user.email],
        )
        email.content_subtype = "html"
        email.send()

