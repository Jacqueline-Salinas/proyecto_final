from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import PerfilCliente

# Registro del modelo PerfilCliente
@admin.register(PerfilCliente)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'nombre', 'apellido', 'nacionalidad', 'correo')
    # Puedes personalizar otros aspectos del modelo en el panel de admin aquí

# Registro del modelo User
admin.site.unregister(User)  # Desregistras el UserAdmin predeterminado
admin.site.register(User, UserAdmin)  # Lo registras nuevamente para personalizarlo si lo deseas
