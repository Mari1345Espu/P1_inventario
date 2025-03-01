from django.db import models

# Create your models here.
from usuarios.models import Cliente
from productos.models import Producto

class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, related_name="pedidos")
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_entrega_estimada = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, default='pendiente')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def calcular_total(self):
        self.total = sum(detalle.subtotal() for detalle in self.detalles.all())
        self.save()

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.usuario.username if self.cliente else 'Cliente Eliminado'}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"Pedido {self.pedido.id} - {self.producto.nombre}"

class SolicitudCotizacion(models.Model):
    ESTADOS_COTIZACION = [
        ('pendiente', 'Pendiente'),
        ('en_revision', 'En Revisión'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, related_name="solicitudes_cotizacion")
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_COTIZACION, default='pendiente')
    total_estimado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pedido_relacionado = models.OneToOneField(Pedido, on_delete=models.SET_NULL, null=True, blank=True)

    def calcular_total(self):
        self.total_estimado = sum(detalle.subtotal() for detalle in self.detalles.all())
        self.save()

    def __str__(self):
        return f"Cotización {self.id} - {self.cliente.usuario.username if self.cliente else 'Cliente Eliminado'}"

class DetalleCotizacion(models.Model):
    solicitud = models.ForeignKey(SolicitudCotizacion, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"Cotización {self.solicitud.id} - {self.producto.nombre}"
