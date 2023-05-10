from django.db import models
from django.utils import timezone

# Create your models here.


class Beneficios(models.Model):
    id_colaborador = models.IntegerField(null=True, blank=True)
    nome = models.CharField(max_length=50)
    vt = models.CharField(null=True, blank=True, max_length=4)
    va = models.CharField(null=True, blank=True, max_length=4)
    saude = models.CharField(null=True, blank=True, max_length=4)
    brinde = models.CharField(null=True, blank=True, max_length=4)
    data_recebimento = models.DateTimeField(blank=True, default=timezone.now)
    data_entrega = models.DateTimeField(null=True)
    data_att = models.DateTimeField(null=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    observacao = models.CharField(max_length=50, null=True, blank=True)
    