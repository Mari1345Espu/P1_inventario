from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
# pedidos/views.py 
from .models import Pedido, DetallePedido, SolicitudCotizacion, DetalleCotizacion
from .forms import PedidoForm, DetallePedidoForm, SolicitudCotizacionForm, DetalleCotizacionForm
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def list_pedidos(request):
    # Verificar si el usuario tiene un cliente asociado
    if hasattr(request.user, 'cliente'):
        pedidos = Pedido.objects.filter(cliente=request.user.cliente).order_by('-fecha_pedido')
    else:
        pedidos = []  # Si no tiene cliente, la lista de pedidos estará vacía

    return render(request, 'pedidos/list_pedidos.html', {'pedidos': pedidos})

def create_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/create_pedido.html', {'form': form})

def update_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('list_pedidos')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedidos/update_pedido.html', {'form': form})

def delete_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('list_pedidos')
    return render(request, 'pedidos/delete_pedido.html', {'pedido': pedido})

def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    detalles = DetallePedido.objects.filter(pedido=pedido)
    return render(request, 'pedidos/detalle_pedido.html', {'pedido': pedido, 'detalles': detalles})

def list_solicitudes_cotizacion(request):
    solicitudes = SolicitudCotizacion.objects.all()
    return render(request, 'pedidos/list_solicitudes_cotizacion.html', {'solicitudes': solicitudes})

def create_solicitud_cotizacion(request):
    if request.method == 'POST':
        form = SolicitudCotizacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_solicitudes_cotizacion')
    else:
        form = SolicitudCotizacionForm()
    return render(request, 'pedidos/create_solicitud_cotizacion.html', {'form': form})

def update_solicitud_cotizacion(request, pk):
    solicitud = get_object_or_404(SolicitudCotizacion, pk=pk)
    if request.method == 'POST':
        form = SolicitudCotizacionForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('list_solicitudes_cotizacion')
    else:
        form = SolicitudCotizacionForm(instance=solicitud)
    return render(request, 'pedidos/update_solicitud_cotizacion.html', {'form': form})

def delete_solicitud_cotizacion(request, pk):
    solicitud = get_object_or_404(SolicitudCotizacion, pk=pk)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('list_solicitudes_cotizacion')
    return render(request, 'pedidos/delete_solicitud_cotizacion.html', {'solicitud': solicitud})

def detalle_solicitud_cotizacion(request, pk):
    solicitud = get_object_or_404(SolicitudCotizacion, pk=pk)
    detalles = DetalleCotizacion.objects.filter(solicitud=solicitud)
    return render(request, 'pedidos/detalle_solicitud_cotizacion.html', {'solicitud': solicitud, 'detalles': detalles})


