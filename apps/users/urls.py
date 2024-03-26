from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("me/", views.me_profile, name="me"),
    path("me/update/", views.update, name="update"),
    path("emails/", views.UserEmailView.as_view(), name="emails"),
    # path("signup/", views.signup, name="signup"),
    # path("signin/", views.SigninView.as_view(redirect_authenticated_user=True), name="signin"),
    # path("signout/", views.signout, name="signout"),
    path("clients/<str:cid>", views.clients_detail, name="clients-detail"),
    # path("activate/<uidb64>/<token>/", views.activate, name="activate"),
    # path(
    #     "request-email-verification/",
    #     views.request_email_verification,
    #     name="request-email-verification",
    # ),
    
]
