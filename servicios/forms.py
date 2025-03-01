# servicios/forms.py
from django import forms
from .models import Servicio, InstalacionServicio, DetalleInstalacionServicio, CheckList

class ServicioForm(forms.ModelForm):
    DISPONIBILIDAD_CHOICES = [
        (True, 'Disponible'),
        (False, 'No Disponible'),
    ]

    disponibilidad = forms.ChoiceField(choices=DISPONIBILIDAD_CHOICES, widget=forms.Select())

    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'precio', 'disponibilidad']
                

class InstalacionServicioForm(forms.ModelForm):
    class Meta:
        model = InstalacionServicio
        fields = ['servicio', 'estado']
        widgets = {
            'estado': forms.Select(choices=InstalacionServicio.ESTADO_CHOICES, attrs={'class': 'form-control'}),
        }

class DetalleInstalacionServicioForm(forms.ModelForm):
    class Meta:
        model = DetalleInstalacionServicio
        fields = ['instalacion', 'descripcion', 'cantidad']

class CheckListForm(forms.ModelForm):
    class Meta:
        model = CheckList
        fields = ['servicio', 'item', 'verificado']
