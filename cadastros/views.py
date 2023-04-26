from django.shortcuts import render, redirect
from recebimentos.models import Setores 
from envios.models import EtiquetaCorreios, CodigoPostagem
# Create your views here.


# Departamentos **********

def cadastro_dep(request):
    departamentos = Setores.objects.all()
    return render(request, "cadastro_dep.html", {"departamentos": departamentos})

def salvar_cadastro_dep(request):
    departamento = request.POST.get("departamento")
    Setores.objects.create(departamento=departamento)
    return redirect(cadastro_dep)

def editar_cadastro_dep(request, id):
    dep = Setores.objects.get(id=id)
    return render(request, "atualizar_cadastro_dep.html", {"dep": dep})


def update_cadastro_dep(request, id):
    ndepartamento = request.POST.get("departamento")
    dep = Setores.objects.get(id=id)
    dep.departamento = ndepartamento
    dep.save()
    """return redirect(home_envio)"""
    return redirect(cadastro_dep)




# Etiqueta Correios **********

def cadastro_etiqueta(request):
    etiqueta = EtiquetaCorreios.objects.all()
    return render(request, "cadastro_etiqueta.html", {"etiqueta": etiqueta})

def salvar_cadastro_etiqueta(request):
    codigo = request.POST.get("Codigo")
    servico = request.POST.get("Servico")
    EtiquetaCorreios.objects.create(codigo=codigo, servico=servico)
    return redirect(cadastro_etiqueta)

def editar_cadastro_etiqueta(request, id):
    etiqueta = EtiquetaCorreios.objects.get(id=id)
    return render(request, "atualizar_cadastro_etiqueta.html", {"etiqueta": etiqueta})


def update_cadastro_etiqueta(request, id):
    nservico = request.POST.get("servico")
    ncodigo = request.POST.get("codigo")
    etiqueta = EtiquetaCorreios.objects.get(id=id)
    etiqueta.servico = nservico
    etiqueta.codigo = ncodigo
    etiqueta.save()
    return redirect(cadastro_etiqueta)






# Codigo Postagem **********

def cadastro_postagem(request):
    post = CodigoPostagem.objects.all()
    dep = Setores.objects.all()
    serv = EtiquetaCorreios.objects.values('servico').distinct()
    return render(request, "cadastro_postagem.html", {"post": post, "dep":dep, "serv":serv})

def salvar_cadastro_postagem(request):
    departamento = request.POST.get("departamento")
    servico = request.POST.get("servico")
    postagem = request.POST.get("postagem")
    departamento1 = Setores.objects.get(departamento=departamento)
    servico1 = EtiquetaCorreios.objects.filter(servico=servico).order_by('servico').first()
    CodigoPostagem.objects.create(departamento=departamento1, servico=servico1, postagem=postagem)
    return redirect(cadastro_postagem)

def editar_cadastro_postagem(request, id):
    post = CodigoPostagem.objects.get(id=id)
    dep = Setores.objects.all()
    serv = EtiquetaCorreios.objects.values('servico').distinct()
    return render(request, "atualizar_cadastro_postagem.html", {"post": post, "dep":dep, "serv":serv})


def update_cadastro_postagem(request, id):
    ndepartamento = request.POST.get("departamento")
    nservico = request.POST.get("servico")
    npostagem = request.POST.get("postagem")
    departamento1 = Setores.objects.get(departamento=ndepartamento)
    servico1 = EtiquetaCorreios.objects.filter(servico=nservico).order_by('servico').first()
    post = CodigoPostagem.objects.get(id=id)
    post.departamento = departamento1
    post.servico = servico1
    post.postagem = npostagem
    post.save()
    return redirect(cadastro_postagem)
    
