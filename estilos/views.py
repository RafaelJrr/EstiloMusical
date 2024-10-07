from django.shortcuts import render, redirect, get_object_or_404
from .models import Estilo

def listar_estilo(request):
    estilo = Estilo.objects.all()
    return render(request,'listarestilo.html',{'estilo': estilo})


def cadastrar_estilo(request):
    if request.method =='POST':
        nome = request.POST['nome']
        Estilo.objects.create(nome=nome)
        return redirect('listar_estilo')
    return render(request, 'formestilo.html')

def editar_estilo(request,id):
    estilo = get_object_or_404(Estilo,id=id)
    if request.method =='POST':
        nome = request.POST['nome']
        return redirect('listar_estilo')
    return render(request, 'formestilo.html',{'estilo': estilo})

def excluir_estilo(request,id):
    estilo = get_object_or_404(Estilo,id=id)
    if request.method =='POST':
        estilo.delete()
        return redirect('listar_estilo')
    return render(request,'confirmar_exclusaoestilo.html',{'estilo': estilo})
    
