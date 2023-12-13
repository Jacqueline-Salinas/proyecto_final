from django.urls import path
from . import views

app_name = "producto"

urlpatterns = [
    path("", views.index, name="index"),
    path('producto/crear_producto/', views.crear_o_actualizar_producto, name="crear_producto"),
    path('producto/crear_proveedor/', views.crear_proveedor, name="crear_proveedor"),
    path('producto/crear_stock/', views.crear_stock, name="crear_stock"),
    path('producto/actualizar/<int:pk>/', views.crear_o_actualizar_producto, name='actualizar_producto'),
    path('producto/borrar/<int:pk>/', views.borrar_producto, name='borrar_producto'),
]
