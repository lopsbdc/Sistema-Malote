from django.shortcuts import render, redirect
from envios.models import Envio

# Create your views here.

def envio_bord(request):
    bd = Envio.objects.all()
    return render(request, 'envio_bord.html', {'bd': bd})

def home_bord(request):
    return render(request, 'home_bord.html')
