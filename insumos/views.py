from django.shortcuts import render, redirect, get_object_or_404
from .models import Insumo
from .forms import InsumoForm

def list_insumos(request):
    insumos = Insumo.objects.all()
    return render(request, 'insumos/list_insumos.html', {'insumos': insumos})

def create_insumo(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_insumos')
    else:
        form = InsumoForm()
    return render(request, 'insumos/create_insumo.html', {'form': form})

def update_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    if request.method == 'POST':
        form = InsumoForm(request.POST, instance=insumo)
        if form.is_valid():
            form.save()
            return redirect('list_insumos')
    else:
        form = InsumoForm(instance=insumo)
    return render(request, 'insumos/update_insumo.html', {'form': form})

def delete_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    if request.method == 'POST':
        insumo.delete()
        return redirect('list_insumos')
    return render(request, 'insumos/delete_insumo.html', {'insumo': insumo})
