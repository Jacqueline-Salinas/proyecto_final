from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PerfilCliente

class ClienteRegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    nacionalidad = forms.CharField(max_length=100)
    correo = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'nombre', 'apellido', 'nacionalidad', 'correo')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()

        if commit:
            # Crear el perfil del cliente asociado al usuario
            perfil_cliente = PerfilCliente.objects.create(
                user=user,
                nombre=self.cleaned_data['nombre'],
                apellido=self.cleaned_data['apellido'],
                nacionalidad=self.cleaned_data['nacionalidad'],
                correo=self.cleaned_data['correo']
            )
        return user
