from django.db import models
from django.utils import timezone
from recebimentos.models import Setores


# Create your models here.

class EtiquetaCorreios(models.Model):
    servico = models.CharField(max_length=50)
    codigo = models.CharField(max_length=2)
    
    def __str__(self):
        return self.servico
    
    
class CodigoPostagem(models.Model):
    departamento = models.ForeignKey(Setores, on_delete=models.PROTECT)
    servico = models.ForeignKey(EtiquetaCorreios, on_delete=models.PROTECT)
    postagem = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.postagem
    
    class Meta:
        unique_together = ('departamento', 'servico',)
    
    

class Envio(models.Model):
    destinatario = models.CharField(max_length=100, null=False)
    remetente = models.CharField(max_length=100)
    rastreio = models.CharField(max_length=100, unique=True, blank=True)
    cep = models.CharField(max_length=100)
    departamento = models.ForeignKey(Setores, on_delete=models.PROTECT)
    servico = models.ForeignKey(EtiquetaCorreios, on_delete=models.PROTECT)
    postagem = models.ForeignKey(CodigoPostagem, on_delete=models.PROTECT)
    data = models.DateTimeField(blank=True, default=timezone.now)
    data_att = models.DateTimeField(null=True)
    
    def __float__(self):
        return self.destinatario


