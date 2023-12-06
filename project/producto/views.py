from django.shortcuts import render
from .forms import *

def home(request):
    return render(request, 'producto/index.html')

def crear_producto(request):
    if request.method == 'GET':
        context = {"form": ProductoForm()}
        return render(request, 'producto/crear_producto.html', context)
        