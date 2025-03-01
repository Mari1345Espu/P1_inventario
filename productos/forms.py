from django import forms
from .models import Producto, Bodega

class ProductoForm(forms.ModelForm):
    bodega = forms.ModelChoiceField(
        queryset=Bodega.objects.all(),  # Cargar todas las bodegas disponibles
        empty_label="Seleccione una bodega",  # Texto predeterminado
        widget=forms.Select(attrs={'class': 'form-select'})  # Estilizado con Bootstrap
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'modelo', 'referencia', 'presentacion', 'especificaciones_tecnicas', 'precio', 'stock', 'stock_minimo', 'bodega']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'referencia': forms.TextInput(attrs={'class': 'form-control'}),
            'presentacion': forms.TextInput(attrs={'class': 'form-control'}),
            'especificaciones_tecnicas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_minimo': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ['nombre', 'direccion', 'ciudad', 'estado', 'codigo_postal']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control'}),
        }
