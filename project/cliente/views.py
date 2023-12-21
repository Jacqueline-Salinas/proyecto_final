from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import ClienteRegistroForm
from .models import PerfilCliente

def registro(request):
    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            # Crear el perfil del cliente asociado al usuario registrado
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            nacionalidad = form.cleaned_data.get('nacionalidad')
            correo = form.cleaned_data.get('correo')
            PerfilCliente.objects.create(user=user, nombre=nombre, apellido=apellido, nacionalidad=nacionalidad, correo=correo)
            # Autenticar al usuario recién registrado
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('nombre_de_la_vista')  # Redirigir a donde desees después del registro
    else:
        form = ClienteRegistroForm()
    return render(request, 'cliente/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('nombre_de_la_vista')  # Redirigir a donde desees después del inicio de sesión
        else:
            # Manejar la lógica para un inicio de sesión fallido
            pass
    return render(request, 'cliente/login.html')
