from django.shortcuts import render, redirect
from .forms import *
from .models import Producto

def home(request):
    return render(request, 'producto/index.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/index.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto:index')
    else:
        form = ProductoForm()
    
    context = {"form": form}
    return render(request, 'producto/crear_producto.html', context)

        