from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from .forms import *
from .models import Producto

def es_admin(user):
    return user.is_superuser

def acceso_denegado(request):
    return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

@user_passes_test(es_admin, login_url='cliente:login')
def home(request):
    return render(request, 'producto/index.html')

@user_passes_test(es_admin, login_url='cliente:login')
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/index.html', {'productos': productos})

@user_passes_test(es_admin, login_url='cliente:login')
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

@user_passes_test(es_admin, login_url='cliente:login')
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

@user_passes_test(es_admin, login_url='cliente:login')
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

@user_passes_test(es_admin, login_url='cliente:login')
def index(request):
    form = BuscarForm()
    productos = Producto.objects.all()

    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            productos = productos.filter(nombre__icontains=nombre)

    return render(request, 'producto/index.html', {'productos': productos, 'form': form})

@user_passes_test(es_admin, login_url='cliente:login')
@require_POST
def borrar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    producto.delete()
    return redirect('producto:index')


        