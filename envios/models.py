from django.db import models
from django.utils import timezone



# Create your models here.

class Envio(models.Model):
    destinatario = models.CharField(max_length=100, null=False)
    remetente = models.CharField(max_length=100)
    rastreio = models.CharField(max_length=100, unique=True, blank=True)
    cep = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    servico = models.CharField(max_length=100)
    cartao = models.CharField(max_length=100)
    data = models.DateTimeField(blank=True, default=timezone.now)
    data_att = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.destinatario
    
    
class EtiquetaCorreios(models.Model):
    codigo = models.CharField(max_length=2)
    servico = models.CharField(max_length=50)


class CodigoPostagem(models.Model):
    setor = models.CharField(max_length=100)
    servico = models.CharField(max_length=50)
    postagem = models.FloatField()