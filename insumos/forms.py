from django import forms
from .models import Insumo

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'cantidad', 'descripcion']
