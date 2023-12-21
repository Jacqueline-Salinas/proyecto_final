from django.urls import path, include

from . import views

app_name = "cliente"

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    # Otros paths que puedas necesitar en esta app
]
