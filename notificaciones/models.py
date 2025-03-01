from django.db import models

# Create your models here.

from usuarios.models import Usuario

class Notificacion(models.Model):
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notificación para {self.usuario.username}"

