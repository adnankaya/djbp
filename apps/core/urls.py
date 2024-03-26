from django.urls import path, include

from . import views

app_name = "core"



urlpatterns = [
    path('set-theme/', views.set_theme, name='set_theme'),
    

]


