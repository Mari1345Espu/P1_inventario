from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from .models import Servicio, InstalacionServicio, DetalleInstalacionServicio, CheckList
from .forms import ServicioForm, InstalacionServicioForm, DetalleInstalacionServicioForm, CheckListForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def list_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/list_servicios.html', {'servicios': servicios})

def create_servicio(request):
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('list_servicios'))  # Redirige después de guardar
        else:
            print(form.errors)  # <-- Esto imprimirá errores en la consola de Django
    else:
        form = ServicioForm()
    
    return render(request, 'servicios/create_servicio.html', {'form': form})

def update_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('list_servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'servicios/update_servicio.html', {'form': form, 'servicio': servicio})

def delete_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('list_servicios')
    return render(request, 'servicios/delete_servicio.html', {'servicio': servicio})

def list_instalaciones(request):
    instalaciones = InstalacionServicio.objects.all()

    # Contar instalaciones por estado
    estados = {
        "Pendiente": InstalacionServicio.objects.filter(estado="Pendiente").count(),
        "Atendida": InstalacionServicio.objects.filter(estado="Atendida").count(),
        "Cancelada": InstalacionServicio.objects.filter(estado="Cancelada").count(),
    }

    return render(request, 'servicios/list_instalaciones.html', {
        'instalaciones': instalaciones,
        'estados': estados
    })



@login_required
def create_instalacion(request):
    if request.user.tipo_usuario != "cliente":
        return redirect('list_instalaciones')  # Solo los clientes pueden crear

    if request.method == "POST":
        form = InstalacionServicioForm(request.POST)
        if form.is_valid():
            instalacion = form.save(commit=False)
            instalacion.cliente = request.user.cliente  # Asigna el cliente automáticamente
            instalacion.save()
            return redirect('list_instalaciones')
    else:
        form = InstalacionServicioForm()

    return render(request, 'create_instalacion.html', {'form': form})


def update_instalacion(request, pk):
    instalacion = get_object_or_404(InstalacionServicio, pk=pk)
    if request.method == 'POST':
        form = InstalacionServicioForm(request.POST, instance=instalacion)
        if form.is_valid():
            form.save()
            return redirect('list_instalaciones')
    else:
        form = InstalacionServicioForm(instance=instalacion)
    return render(request, 'servicios/update_instalacion.html', {'form': form})

def delete_instalacion(request, pk):
    instalacion = get_object_or_404(InstalacionServicio, pk=pk)
    if request.method == 'POST':
        instalacion.delete()
        return redirect('list_instalaciones')
    return render(request, 'servicios/delete_instalacion.html', {'instalacion': instalacion})

def detalle_instalacion(request, pk):
    instalacion = get_object_or_404(InstalacionServicio, pk=pk)
    detalles = DetalleInstalacionServicio.objects.filter(instalacion=instalacion)
    return render(request, 'servicios/detalle_instalacion.html', {'instalacion': instalacion, 'detalles': detalles})

def list_checklists(request):
    checklists = CheckList.objects.all()
    return render(request, 'servicios/list_checklists.html', {'checklists': checklists})

def create_checklist(request):
    if request.method == 'POST':
        form = CheckListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_checklists')
    else:
        form = CheckListForm()
    return render(request, 'servicios/create_checklist.html', {'form': form})

def update_checklist(request, pk):
    checklist = get_object_or_404(CheckList, pk=pk)
    if request.method == 'POST':
        form = CheckListForm(request.POST, instance=checklist)
        if form.is_valid():
            form.save()
            return redirect('list_checklists')
    else:
        form = CheckListForm(instance=checklist)
    return render(request, 'servicios/update_checklist.html', {'form': form})

def delete_checklist(request, pk):
    checklist = get_object_or_404(CheckList, pk=pk)
    if request.method == 'POST':
        checklist.delete()
        return redirect('list_checklists')
    return render(request, 'servicios/delete_checklist.html', {'checklist': checklist})



