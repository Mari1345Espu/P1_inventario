from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import Notificacion
from .forms import NotificacionForm

def list_notificaciones(request):
    notificaciones = Notificacion.objects.all()
    return render(request, 'notificaciones/list_notificaciones.html', {'notificaciones': notificaciones})

def create_notificacion(request):
    if request.method == 'POST':
        form = NotificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_notificaciones')
    else:
        form = NotificacionForm()
    return render(request, 'notificaciones/create_notificacion.html', {'form': form})

def update_notificacion(request, pk):
    notificacion = get_object_or_404(Notificacion, pk=pk)
    if request.method == 'POST':
        form = NotificacionForm(request.POST, instance=notificacion)
        if form.is_valid():
            form.save()
            return redirect('list_notificaciones')
    else:
        form = NotificacionForm(instance=notificacion)
    return render(request, 'notificaciones/update_notificacion.html', {'form': form})

def delete_notificacion(request, pk):
    notificacion = get_object_or_404(Notificacion, pk=pk)
    if request.method == 'POST':
        notificacion.delete()
        return redirect('list_notificaciones')
    return render(request, 'notificaciones/delete_notificacion.html', {'notificacion': notificacion})
