from django.shortcuts import render
from producto.models import Producto

def home(request):
    productos = Producto.objects.all()
    return render(request, 'core/index.html', {'productos': productos})

def about(request):
    return render(request, 'core/about.html')
