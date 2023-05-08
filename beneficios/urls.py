from django.contrib import admin
from django.urls import path, include
from .views import home_beneficios, cadastro_beneficio, salvar_beneficio, update_beneficio, delete_beneficio, editar_beneficio

urlpatterns = [
    #path('cadastro_beneficio', cadastro_beneficios),
    path('', home_beneficios),
    path('editar_beneficio/<int:id>', editar_beneficio, name="editar_beneficio"),
    path('cadastro/', cadastro_beneficio, name="cadastro_beneficio"),
    path('salvar_beneficio/', salvar_beneficio, name="salvar_beneficio"),
    path('update_beneficio/<int:id>', update_beneficio, name="update_beneficio"),
    path('delete_beneficio/<int:id>', delete_beneficio, name="delete_beneficio"),
]