import django_filters

from .models import Envio

class EnvioFilter(django_filters.FilterSet):
    
    class Meta:
        model = Envio
        fields = [
            'destinatario',
            'remetente',
            'rastreio',
            'data',
        ]