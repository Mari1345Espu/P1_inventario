from django.db import models
# Create your models here

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    descripcion = models.TextField()
    
    class Meta:
        app_label = 'insumos'

    def __str__(self):
        return self.nombre

