from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "cliente"

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL y vista de cierre de sesión
    # Otros paths que puedas necesitar en esta app
]
