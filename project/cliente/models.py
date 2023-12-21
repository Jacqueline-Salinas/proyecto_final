from django.contrib.auth.models import User
from django.db import models

class PerfilCliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.user.username}'s Profile"
