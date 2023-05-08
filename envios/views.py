from django.shortcuts import render, redirect
from .models import Envio, EtiquetaCorreios, CodigoPostagem, Setores
from .filters import EnvioFilter
from django.core.paginator import Paginator
from django_datatables_view import base_datatable_view
from django.utils.html import escape
from datetime import datetime

# Create your views here.

def index1(request):
    bd = Envio.objects.all()
    return render(request, 'vista.html', {'bd': bd})


def home_envio(request):
    envios = Envio.objects.all()
    departamento = request.GET.get('departamento')
    servico = request.GET.get('servico')
    serv = EtiquetaCorreios.objects.values('servico').distinct()
    dep = Setores.objects.all()
    post = CodigoPostagem.objects.filter(departamento=departamento, servico=servico)
    ultimo = Envio.objects.all().order_by('-id')[:3]
    return render(request, "envios.html", {"envios": envios, "post":post, "serv":serv, "dep":dep, "ultimo":ultimo})


def salvar_envio(request):
    destinatario = request.POST.get("destinatario")
    remetente = request.POST.get("remetente")
    rastreio = request.POST.get("rastreio")
    cep = request.POST.get("cep")
    departamento = Setores.objects.get(departamento = request.POST.get("departamento"))
    codigo = str(rastreio[:2])
    servico = EtiquetaCorreios.objects.get(codigo=codigo)
    postagem = CodigoPostagem.objects.get(departamento=departamento, servico__servico=servico)
    Envio.objects.create(destinatario=destinatario, rastreio=rastreio, remetente=remetente, cep=cep, departamento=departamento, servico=servico, postagem=postagem)
    return redirect(home_envio)


def editar_envio(request, id):
    envio = Envio.objects.get(id=id)
    dep = Setores.objects.all()
    return render(request, "atualizar.html", {"envio": envio, "dep":dep})


def update_envio(request, id):
    ndestinatario = request.POST.get("destinatario")
    nrastreio = request.POST.get("rastreio")
    nremetente = request.POST.get("remetente")
    ncep = request.POST.get("cep")
    ndepartamento = Setores.objects.filter(departamento = request.POST.get("departamento")).first()
    codigo = str(nrastreio[:2])
    nservico = EtiquetaCorreios.objects.get(codigo=codigo)
    postagem = CodigoPostagem.objects.get(departamento=ndepartamento, servico__servico=nservico)
    envio = Envio.objects.get(id=id)
    envio.cep = ncep
    envio.departamento = ndepartamento
    envio.servico = nservico
    envio.destinatario = ndestinatario
    envio.remetente = nremetente
    envio.rastreio = nrastreio
    envio.postagem = postagem
    envio.data_att = datetime.now()
    envio.save()
    """return redirect(home_envio)"""
    return redirect(index1)


def delete_envio(request, id):
    envio = Envio.objects.get(id=id)
    envio.delete()
    """return redirect(home_envio)"""
    return redirect(index1)


# def mostrar_envios(request):
#     context = {}
    
#     filtrados = EnvioFilter(
#         request.GET,
#         queryset = Envio.objects.all()        
#     )
    
#     context['filtrados'] = filtrados
    
#     filtro_paginado = Paginator(filtrados.qs, 2)
#     num_paginas = request.GET.get('page')
#     filtro_obj = filtro_paginado.get_page(num_paginas)
    
#     context['filtro_obj'] = filtro_obj
    
#     return render(request, 'filtro.html', context=context)
    
""" def mostrar_envios(request):
    class OrderListJson(base_datatable_view):
        model = Envio
        columns = ['destinatario', 'remetente', 'rastreio', 'data']
        order_columns = ['destinatario', 'remetente', 'rastreio', 'data']
        max_display_length = 50       
        
        
        Essa é a próxima parte, criar um datatable pra filtrar e paginar """    
