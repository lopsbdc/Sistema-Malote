from django.shortcuts import render, redirect
from envios.models import Envio
from recebimentos.models import Recebidos

# Create your views here.

def envio_bord(request):
    bd = Envio.objects.all()
    return render(request, 'envio_bord.html', {'bd': bd})

def recebido_bord(request):
    bd = Recebidos.objects.all()
    return render(request, 'recebido_bord.html', {'bd': bd})
