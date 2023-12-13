from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from .forms import *
from .models import Producto

def home(request):
    return render(request, 'producto/index.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/index.html', {'productos': productos})

def crear_o_actualizar_producto(request, pk=None):
    producto = get_object_or_404(Producto, pk=pk) if pk else None
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto:index')  # Reemplaza 'producto:index' con la URL adecuada
    else:
        form = ProductoForm(instance=producto)
    
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
            # Guarda el formulario y obtiene los datos
            stock = form.save(commit=False)
            producto = stock.producto
            cantidad = stock.cantidad

            # Actualiza la cantidad de stock en el Producto asociado
            producto.stock += cantidad
            producto.save()

            stock.save()  # Guarda el objeto Stock
            return redirect('producto:index')
    else:
        form = StockForm()
    
    context = {"form": form}
    return render(request, 'producto/crear_stock.html', context)

def index(request):
    form = BuscarForm()
    productos = Producto.objects.all()

    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            productos = productos.filter(nombre__icontains=nombre)

    return render(request, 'producto/index.html', {'productos': productos, 'form': form})

@require_POST
def borrar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    producto.delete()
    return redirect('lista_productos')

        