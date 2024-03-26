import logging
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


logger = logging.getLogger("db")


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def on_authentication_error(
        self, request, provider, error=None, exception=None, extra_context=None
    ):
        super().on_authentication_error(
            request, provider, error, exception, extra_context
        )
        logger.error(
            f"Social authentication error! , error:{error}, request={request}",
            extra={
                "provider": provider,
                "error": error.__str__(),
                "exception": exception.__str__(),
                "extra_context": extra_context,
            },
        )
