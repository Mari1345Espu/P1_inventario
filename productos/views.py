from django.shortcuts import render, redirect, get_object_or_404

# Create your views here. 
from .models import Producto, Bodega
from .forms import ProductoForm, BodegaForm
from django.contrib import messages

def list_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/list_productos.html', {'productos': productos})

def create_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/create_producto.html', {'form': form, 'bodegas': Bodega })

def update_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('list_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/update_producto.html', {'form': form})

def delete_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('list_productos')
    return render(request, 'productos/delete_producto.html', {'producto': producto})



def add_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    # Obtener carrito desde la sesión
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)]['cantidad'] += 1
    else:
        carrito[str(producto_id)] = {
            'nombre': producto.nombre,
            'precio': float(producto.precio),
            'cantidad': 1
        }


    # Guardamos el carrito en la sesión
    request.session['carrito'] = carrito
    return redirect('ver_carrito')  # Redirige a la vista donde se muestra el carrito

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    
    # Calcular el total general del carrito
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())

    return render(request, 'carrito.html', {'carrito': carrito, 'total': total})

def remove_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        del carrito[str(producto_id)]  # Eliminar producto

    request.session['carrito'] = carrito
    return redirect('ver_carrito')

def increase_quantity(request, producto_id):
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)]['cantidad'] += 1

    request.session['carrito'] = carrito
    return redirect('ver_carrito')

def decrease_quantity(request, producto_id):
    carrito = request.session.get('carrito', {})

    if str(producto_id) in carrito:
        if carrito[str(producto_id)]['cantidad'] > 1:
            carrito[str(producto_id)]['cantidad'] -= 1
        else:
            del carrito[str(producto_id)]  # Eliminar si llega a 0

    request.session['carrito'] = carrito
    return redirect('ver_carrito')


def list_bodegas(request):
    bodegas = Bodega.objects.all()
    return render(request, 'productos/list_bodegas.html', {'bodegas': bodegas})

def create_bodega(request):
    if request.method == 'POST':
        form = BodegaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_bodegas')
    else:
        form = BodegaForm()
    return render(request, 'productos/create_bodega.html', {'form': form})

def update_bodega(request, pk):
    bodega = get_object_or_404(Bodega, pk=pk)
    if request.method == 'POST':
        form = BodegaForm(request.POST, instance=bodega)
        if form.is_valid():
            form.save()
            return redirect('list_bodegas')
    else:
        form = BodegaForm(instance=bodega)
    return render(request, 'productos/update_bodega.html', {'form': form})

def delete_bodega(request, pk):
    bodega = get_object_or_404(Bodega, pk=pk)
    if request.method == 'POST':
        bodega.delete()
        return redirect('list_bodegas')
    return render(request, 'productos/delete_bodega.html', {'bodega': bodega})

