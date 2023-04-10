from django.shortcuts import render, redirect
from .models import Recebidos
from datetime import datetime

# Create your views here.

def cadastro(request):
    ultimos_registros = Recebidos.objects.all().order_by('-id')[:3]
    return render(request, 'cadastro.html', {'ultimos_registros': ultimos_registros})


def salvar_recebimento(request):
    destinatario = request.POST.get("destinatario")
    remetente = request.POST.get("remetente")
    rastreio = request.POST.get("rastreio")
    cep_remetente = request.POST.get("cep_remetente")
    tipo = request.POST.get("tipo")
    ar_anexa = request.POST.get("ar_anexa")
    departamento = request.POST.get("departamento")
    obs = request.POST.get("obs")
    status = "Não entregue"
    Recebidos.objects.create(destinatario=destinatario, rastreio=rastreio, remetente=remetente, cep_remetente=cep_remetente, 
                             tipo=tipo, ar_anexa=ar_anexa, departamento=departamento, status=status, observacao=obs)
    return redirect(cadastro)


def salvar_detalhe_recebimento(request, id):
    ndestinatario = request.POST.get("destinatario")
    nrastreio = request.POST.get("rastreio")
    nremetente = request.POST.get("remetente")
    ncep = request.POST.get("cep_remetente")
    obs = request.POST.get("obs")
    ntipo = request.POST.get("tipo")
    nar = request.POST.get("ar_anexa")
    ndep = request.POST.get("departamento")
    ndata = request.POST.get("data_entrega")
    nstatus = request.POST.get("status")
    nforma = request.POST.get("forma_entrega")
    recebido = Recebidos.objects.get(id=id)
    
    # Se a data for nula, o Django não identifica sempre recusa. então é melhor nem passar nada, deixar blank
    if ndata == "":
        recebido.destinatario = ndestinatario
        recebido.remetente = nremetente
        recebido.rastreio = nrastreio
        recebido.data_att = datetime.now()
        recebido.forma_entrega = nforma
        recebido.status = nstatus
        recebido.departamento = ndep
        recebido.ar_anexa = nar
        recebido.tipo = ntipo
        recebido.cep_remetente = ncep
        recebido.observacao = obs
        recebido.save()
        
    else:
        recebido.destinatario = ndestinatario
        recebido.remetente = nremetente
        recebido.rastreio = nrastreio
        recebido.data_att = datetime.now()
        recebido.data_entrega = ndata
        recebido.forma_entrega = nforma
        recebido.status = nstatus
        recebido.departamento = ndep
        recebido.ar_anexa = nar
        recebido.tipo = ntipo
        recebido.observacao = obs
        recebido.cep_remetente = ncep
        recebido.save()
    return redirect(cadastro)


def detalhe_recebimento(request, id):
    recebido = Recebidos.objects.get(id=id)
    return render(request, "atualizar_recebido.html", {"recebido": recebido})


def delete_recebimento(request, id):
    recebido = Recebidos.objects.get(id=id)
    recebido.delete()
    return redirect(cadastro)


def index2(request):
    recibos = Recebidos.objects.all()
    return render(request, 'vista_recebimento.html', {'recibos': recibos})