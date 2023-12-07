from django.shortcuts import render
from .forms import *

def home(request):
    return render(request, 'producto/index.html')

from django.shortcuts import render, redirect
from .forms import ProductoForm

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

        