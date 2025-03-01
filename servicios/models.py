from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class InstalacionServicio(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('terminada', 'Terminada'),
        ('cancelada', 'Cancelada'),
    ]
    
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    cliente = models.ForeignKey('usuarios.Cliente', on_delete=models.CASCADE)
    fecha_instalacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Instalación de {self.servicio.nombre} para {self.cliente.usuario.username}"

class DetalleInstalacionServicio(models.Model):
    instalacion = models.ForeignKey(InstalacionServicio, on_delete=models.CASCADE)
    descripcion = models.TextField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Detalle de {self.instalacion.servicio.nombre}"

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class CheckList(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    verificado = models.BooleanField(default=False)

    def __str__(self):
        return f"Checklist de {self.servicio.nombre}"

