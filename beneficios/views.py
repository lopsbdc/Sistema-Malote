from django.shortcuts import render, redirect
from .models import Beneficios
from datetime import datetime

# Create your views here.

def home_beneficios(request):
    bd = Beneficios.objects.all()
    return render(request, 'home_beneficios.html', {'bd': bd})

def detalhe_beneficio(request, id):
    bene = Beneficios.objects.get(id=id)
    return render(request, "atualizar_beneficio.html", {'bene':bene})

def cadastro_beneficio(request):
    return render(request, "cadastro_beneficio.html")

def salvar_beneficio(request):
    nome = request.POST.get("nome")
    id_colaborador = request.POST.get("id_colaborador")
    
    if id_colaborador == "":
        id_colaborador = 0
    
    vt = request.POST.get("vt")
    va = request.POST.get("va")
    saude = request.POST.get("saude")
    brinde = request.POST.get("brinde")
    observacao = request.POST.get("observacao")
    status = "Não entregue"
    
    if vt == "on":
        vt = True      
        
    if va == "on":
        va = True      
        
    if saude == "on":
        saude = True     
        
    if brinde == "on":
        brinde = True
        
               
    Beneficios.objects.create(nome=nome, id_colaborador=id_colaborador, vt=vt, va=va, 
                             saude=saude, brinde=brinde, observacao=observacao, status=status)
    return redirect(cadastro_beneficio)



def update_beneficio(request, id):
    nid = request.POST.get("id_colaborador")
    nnome = request.POST.get("nome")
    nvt = request.POST.get("vt")
    nva = request.POST.get("va")
    nsaude = request.POST.get("saude")
    nbrinde = request.POST.get("brinde")
    nstatus = request.POST.get("status")
    nobservacao = request.POST.get("observacao")
    
    if nvt == "on":
        nvt = True       
        
    if nva == "on":
        nva = True      
        
    if nsaude == "on":
        nsaude = True     
        
    if nbrinde == "on":
        nbrinde = True
        
    
    beneficio = Beneficios.objects.get(id=id)
    beneficio.id_colaborador = nid
    beneficio.nome = nnome
    beneficio.vt = nvt
    beneficio.va = nva
    beneficio.saude = nsaude
    beneficio.brinde = nbrinde
    beneficio.status = nstatus
    beneficio.observacao = nobservacao
    beneficio.data_att = datetime.now()
    beneficio.save()
    
    return redirect(home_beneficios)



def delete_beneficio(request, id):
    beneficio = Beneficios.objects.get(id=id)
    beneficio.delete()
    return redirect(home_beneficios)


def editar_beneficio(request, id):
    beneficio = Beneficios.objects.get(id=id)
    return render(request, "atualizar_beneficio.html", {"beneficio": beneficio})