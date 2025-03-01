from django import forms
from .models import Pedido, DetallePedido, SolicitudCotizacion, DetalleCotizacion

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'fecha_entrega_estimada', 'estado']

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model = DetallePedido
        fields = ['pedido', 'producto', 'cantidad', 'precio_unitario']

class SolicitudCotizacionForm(forms.ModelForm):
    class Meta:
        model = SolicitudCotizacion
        fields = ['cliente', 'estado']

class DetalleCotizacionForm(forms.ModelForm):
    class Meta:
        model = DetalleCotizacion
        fields = ['solicitud', 'producto', 'cantidad', 'precio_unitario']
