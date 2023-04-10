from django.db import models
from django.utils import timezone


# Create your models here.

class Recebidos(models.Model):
    destinatario = models.CharField(max_length=100, null=False)
    tipo = models.CharField(max_length=100,null=True)
    remetente = models.CharField(max_length=100,null=True)
    cep_remetente = models.CharField(max_length=100,null=True)
    rastreio = models.CharField(max_length=100,null=True, unique=True, blank=True)
    ar_anexa = models.CharField(max_length=100,null=True)
    departamento = models.CharField(max_length=100,null=True)
    data_recebimento = models.DateTimeField (default=timezone.now, blank=True)
    data_att = models.DateTimeField(null=True)
    status = models.CharField(max_length=100,null=True)
    forma_entrega = models.CharField(max_length=100,null=True)
    data_entrega = models.DateField(blank=True, null=True)
    observacao = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.destinatario
    
    