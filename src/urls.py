from django.contrib import admin
from django.urls import path, include

from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path("admin-djbp/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    path("users/", include("apps.users.urls")),
    path("accounts/", include("allauth.urls")),
    # home
    path("", include("apps.home.urls")),
)
# NOTE TODO if you want to see static files locally while DEBUG=False then uncomment followings
# from django.urls import re_path
# from django.conf import settings
# from django.views.static import serve


# urlpatterns += [
#     # re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
#     re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
# ]
