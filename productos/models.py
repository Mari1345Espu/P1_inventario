from django.db import models

# Create your models here.

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    referencia = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=100)
    especificaciones_tecnicas = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    stock_minimo = models.IntegerField()
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

