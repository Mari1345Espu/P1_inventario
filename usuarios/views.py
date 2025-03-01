from collections import UserList
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here. 
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UsuarioCreationForm, UsuarioChangeForm, ClienteForm, RepartidorForm, MiembroCuadrillaForm, AdministrativoForm, UsuariosForm
from .models import Usuario, Cliente, Repartidor, MiembroCuadrilla, Administrativo

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')  # Si no hay `next`, redirige a 'home'
            return redirect(next_url)
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UsuarioCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'usuarios/profile.html')

@login_required
def list_usuarios(request):
    if not request.user.is_superuser and request.user.tipo_usuario != "administrador":
        return redirect('home')  # Evita que usuarios no autorizados accedan

    usuarios = Usuario.objects.all()  # Obtiene todos los usuarios
    return render(request, 'usuarios/list_usuarios.html', {'usuarios': usuarios})

@login_required
def create_usuarios(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Guardar contraseña encriptada
            user.save()
            messages.success(request, "Usuario creado exitosamente.")
            return redirect('list_usuarios')  # Asegúrate de que esta URL existe
        else:
            messages.error(request, "Error al crear usuario. Verifica los datos.")
    else:
        form = UsuariosForm()

    return render(request, 'usuarios/create_usuarios.html', {'form': form})


@login_required
def edit_usuarios(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)  # Busca el usuario o lanza error 404
    
    if request.method == 'POST':
        form = UsuarioChangeForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario actualizado correctamente")
            return redirect('list_usuarios')
    else:
        form = UsuarioChangeForm(instance=usuario)
    
    return render(request, 'usuarios/edit_usuarios.html', {'form': form, 'usuario': usuario})

@login_required
@user_passes_test(lambda u: u.is_superuser)  # Solo admin puede eliminar usuarios
def delate_usuarios(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)  # Buscar usuario o mostrar error 404

    if request.method == 'POST':  # Confirmar eliminación
        usuario.delete()
        messages.success(request, "Usuario eliminado correctamente.")
        return redirect('list_usuarios')  # Redirigir a la lista de usuarios

    return render(request, 'usuarios/delete_usuarios.html', {'usuario': usuario})


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UsuarioChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente")
            return redirect('profile')  # Redirige al perfil después de actualizar
        else:
            messages.error(request, "Hubo un error en la actualización, revisa los datos")
    else:
        form = UsuarioChangeForm(instance=request.user)
    return render(request, 'usuarios/update_profile.html', {'form': form})

@login_required
def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'usuarios/cliente_detail.html', {'cliente': cliente})

@login_required
def repartidor_detail(request, pk):
    repartidor = get_object_or_404(Repartidor, pk=pk)
    return render(request, 'usuarios/repartidor_detail.html', {'repartidor': repartidor})

@login_required
def miembro_cuadrilla_detail(request, pk):
    miembro_cuadrilla = get_object_or_404(MiembroCuadrilla, pk=pk)
    return render(request, 'usuarios/miembro_cuadrilla_detail.html', {'miembro_cuadrilla': miembro_cuadrilla})

@login_required
def administrativo_detail(request, pk):
    administrativo = get_object_or_404(Administrativo, pk=pk)
    return render(request, 'usuarios/administrativo_detail.html', {'administrativo': administrativo})
