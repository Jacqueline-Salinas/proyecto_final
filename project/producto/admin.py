from django.contrib import admin
from .models import Producto, Proveedor, Stock

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Stock)
