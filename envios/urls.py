from django.contrib import admin
from django.urls import path, include
from .views import home_envio, salvar_envio, editar_envio, update_envio, delete_envio, index1

urlpatterns = [
    path('', index1),
    path('cadastro', home_envio),
    path('salvar_envio/', salvar_envio, name="salvar_envio"),
    path('editar_envio/<int:id>', editar_envio, name="editar_envio"),
    path('update_envio/<int:id>', update_envio, name="update_envio"),
    path('delete_envio/<int:id>', delete_envio, name="delete_envio"),
    #path('consulta/', mostrar_envios),
]
