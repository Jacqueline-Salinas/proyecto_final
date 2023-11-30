from django.urls import path, include

from . import views

app_name = "cliente"

urlpatterns = [
    path('', views.home, name="index"),
]
