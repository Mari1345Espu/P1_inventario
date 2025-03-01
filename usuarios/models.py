from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission  # Importa Group y Permission

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('cliente', 'Cliente'),
        ('administrativo', 'Administrativo'),
        ('administrador', 'Administrador'),
        ('repartidor', 'Repartidor'),
        ('cuadrilla', 'Cuadrilla'),
    ]
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='cliente')
    foto_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)

    # Campos obligatorios para AbstractUser con related_name
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="usuarios_groups"  # Importante: Evita conflictos
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="usuarios_user_permissions"  # Importante: Evita conflictos
    )

class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)

class Repartidor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    disponibilidad = models.BooleanField(default=True)
    bodega = models.ForeignKey('productos.Bodega', on_delete=models.CASCADE)  # Asegúrate que 'productos.Bodega' exista

class MiembroCuadrilla(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    cuadrilla = models.ForeignKey('cuadrillas.Cuadrilla', on_delete=models.CASCADE) # Asegúrate que 'cuadrillas.Cuadrilla' exista
    rol = models.CharField(max_length=50)

class Administrativo(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)