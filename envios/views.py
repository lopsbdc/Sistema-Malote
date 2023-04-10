from django.shortcuts import render, redirect
from .models import Envio, EtiquetaCorreios, CodigoPostagem
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
    return render(request, "envios.html", {"envios": envios})


def salvar_envio(request):
    destinatario = request.POST.get("destinatario")
    remetente = request.POST.get("remetente")
    rastreio = request.POST.get("rastreio")
    departamento = request.POST.get("departamento")
    etiqueta = rastreio[2]
    servico = EtiquetaCorreios.objects.get(servico=etiqueta)
    cartao = "teste"
    Envio.objects.create(destinatario=destinatario, rastreio=rastreio, remetente=remetente)
    return redirect(home_envio)


def editar_envio(request, id):
    envio = Envio.objects.get(id=id)
    return render(request, "atualizar.html", {"envio": envio})


def update_envio(request, id):
    ndestinatario = request.POST.get("destinatario")
    nrastreio = request.POST.get("rastreio")
    nremetente = request.POST.get("remetente")
    envio = Envio.objects.get(id=id)
    envio.destinatario = ndestinatario
    envio.remetente = nremetente
    envio.rastreio = nrastreio
    envio.data_att = datetime.now()
    envio.save()
    """return redirect(home_envio)"""
    return redirect(index1)


def delete_envio(request, id):
    envio = Envio.objects.get(id=id)
    envio.delete()
    """return redirect(home_envio)"""
    return redirect(index1)


def mostrar_envios(request):
    context = {}
    
    filtrados = EnvioFilter(
        request.GET,
        queryset = Envio.objects.all()        
    )
    
    context['filtrados'] = filtrados
    
    filtro_paginado = Paginator(filtrados.qs, 2)
    num_paginas = request.GET.get('page')
    filtro_obj = filtro_paginado.get_page(num_paginas)
    
    context['filtro_obj'] = filtro_obj
    
    return render(request, 'filtro.html', context=context)
    
""" def mostrar_envios(request):
    class OrderListJson(base_datatable_view):
        model = Envio
        columns = ['destinatario', 'remetente', 'rastreio', 'data']
        order_columns = ['destinatario', 'remetente', 'rastreio', 'data']
        max_display_length = 50       
        
        
        Essa é a próxima parte, criar um datatable pra filtrar e paginar """    
