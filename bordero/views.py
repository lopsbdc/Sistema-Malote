from django.shortcuts import render
from envios.models import Envio
from recebimentos.models import Recebidos
from django.utils import timezone
from datetime import datetime
from django.db.models import Q

# Create your views here.

def envio_bord(request):
    today_min = datetime.combine(timezone.now().date(), datetime.today().time().min)
    today_max = datetime.combine(timezone.now().date(), datetime.today().time().max)
    bd = Envio.objects.filter(data__range=(today_min, today_max))  # Para filtrar o dia de hoje, precisa pegar a hora inicio e fim
    total = Envio.objects.filter(data__range=(today_min, today_max)).count()
    date = bd.first()
    hoje = date.data.strftime("%d/%m/%y")
    return render(request, 'envio_bord.html', {'bd': bd, 'total': total, 'hoje':hoje})

def recebido_bord(request):
    bd = Recebidos.objects.filter(~Q(status='Entregue'))  # ~Q funciona como negação da operação lógica
    return render(request, 'recebido_bord.html', {'bd': bd})
