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

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto:index')
    else:
        form = ProveedorForm()
    
    context = {"form": form}
    return render(request, 'producto/crear_proveedor.html', context)

def crear_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto:index')
    else:
        form = StockForm()
    
    context = {"form": form}
    return render(request, 'producto/crear_stock.html', context)

        