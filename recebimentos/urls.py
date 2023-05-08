from django.contrib import admin
from django.urls import path, include
from .views import cadastro, salvar_recebimento, detalhe_recebimento, salvar_detalhe_recebimento, delete_recebimento, index2

urlpatterns = [
    path('cadastro/', cadastro),
    path('salvar_recebimento/', salvar_recebimento, name="salvar_recebimento"),
    path('detalhe_recebimento/<int:id>', detalhe_recebimento, name="detalhe_recebimento"),
    path('salvar_detalhe_recebimento/<int:id>', salvar_detalhe_recebimento, name="salvar_detalhe_recebimento"),
    path('delete_recebimento/<int:id>', delete_recebimento, name="delete_recebimento"),
    path('', index2),
]
