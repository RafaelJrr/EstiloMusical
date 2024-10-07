from django.shortcuts import get_object_or_404, redirect, render
from cantores.forms import  CantoresForm
from cantores.models import Cantores

def listar_cantores(request):
    cantores = Cantores.objects.all()
    return render(request,'listarcantor.html',{'cantores': cantores})

def cadastrar_cantor(request):
    if request.method == "POST":
        form = CantoresForm(request.POST,)
        if form.is_valid():
           form.save()
           return redirect('listar_cantores')
    else:
        form = CantoresForm()
    return render(request,'formcantor.html',{'form':form})

def editar_cantor(request, id):
    cantor = get_object_or_404(Cantores,id=id)
    if request.method == "POST":
        form = CantoresForm(request.POST, instance=cantor)
        if form.is_valid():
            form.save()
            return redirect('listar_cantores')
    else:
        form = CantoresForm(instance=cantor)
    return render(request, 'formcantor.html',{'form':form})

def excluir_cantor(request, id):
    cantor = get_object_or_404(Cantores, id=id)
    if request.method == "POST":
        cantor.delete()
        return redirect('listar_cantor')
    return render(request, 'confirmar_ex_cantor.html', {'cantor':cantor})