from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ClienteRegistroForm
from .models import PerfilCliente

def registro(request):
    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardar el usuario
            perfil_cliente = get_object_or_404(PerfilCliente, user=user)
            if not perfil_cliente:  # Si no existe, crea uno nuevo
                perfil_cliente = PerfilCliente.objects.create(
                    user=user,
                    nombre=form.cleaned_data.get('nombre'),
                    apellido=form.cleaned_data.get('apellido'),
                    nacionalidad=form.cleaned_data.get('nacionalidad'),
                    correo=form.cleaned_data.get('correo')
                )
            # Autenticar al usuario recién registrado si es necesario
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            if request.user.is_authenticated:  # Verificar si el usuario está autenticado
                return redirect('core:index')  # Redirigir al home principal si está autenticado
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
            if not user.is_superuser:  # Si el usuario no es un superusuario
                return redirect('core:index')  # Redirige al home principal
            else:
                return redirect('dashboard_admin')  # Redirige al dashboard de admin si es el superusuario
        # Si el usuario es None o la autenticación falla, puede ser útil agregar un mensaje de error
        else:
            # Manejar la lógica para un inicio de sesión fallido
            pass
    return render(request, 'cliente/login.html')
