from django import forms
from .models import Proveedor, Producto, Stock

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'  # Puedes especificar los campos si no quieres incluirlos todos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'  # Puedes especificar los campos si no quieres incluirlos todos

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'  # Puedes especificar los campos si no quieres incluirlos todos

class BuscarForm(forms.Form):
    nombre = forms.CharField()
