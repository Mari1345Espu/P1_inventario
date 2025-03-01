from django.db import models

# Create your models here.

class Cuadrilla(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class AsignacionCuadrilla(models.Model):
    cuadrilla = models.ForeignKey(Cuadrilla, on_delete=models.CASCADE)
    miembro = models.ForeignKey('usuarios.MiembroCuadrilla', on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Asignación de {self.miembro.usuario.username} a {self.cuadrilla.nombre}"

