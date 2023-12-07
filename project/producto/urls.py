from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path("", views.lista_productos, name="index"),
    path('producto/crear_producto/', views.crear_producto, name="crear_producto"),
    path('producto/crear_proveedor/', views.crear_proveedor, name="crear_proveedor"),
    path('producto/crear_stock/', views.crear_stock, name="crear_stock"),
]
