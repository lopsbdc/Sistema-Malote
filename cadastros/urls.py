from django.contrib import admin
from django.urls import path
from .views import cadastro_dep, salvar_cadastro_dep, editar_cadastro_dep, update_cadastro_dep, cadastro_etiqueta,          salvar_cadastro_etiqueta, update_cadastro_etiqueta, editar_cadastro_etiqueta, salvar_cadastro_postagem, editar_cadastro_postagem, update_cadastro_postagem, cadastro_postagem




urlpatterns = [
    path('departamento/', cadastro_dep),
    path('salvar_cadastro_dep/', salvar_cadastro_dep, name="salvar_cadastro_dep"),
    path('editar_cadastro_dep/<int:id>', editar_cadastro_dep, name="editar_cadastro_dep"),
    path('update_cadastro_dep/<int:id>', update_cadastro_dep, name="update_cadastro_dep"),
    
    path('etiqueta/', cadastro_etiqueta),
    path('salvar_cadastro_etiqueta/', salvar_cadastro_etiqueta, name="salvar_cadastro_etiqueta"),
    path('editar_cadastro_etiqueta/<int:id>', editar_cadastro_etiqueta, name="editar_cadastro_etiqueta"),
    path('update_cadastro_etiqueta/<int:id>', update_cadastro_etiqueta, name="update_cadastro_etiqueta"),

    path('postagem/', cadastro_postagem),
    path('salvar_cadastro_postagem/', salvar_cadastro_postagem, name="salvar_cadastro_postagem"),
    path('editar_cadastro_postagem/<int:id>', editar_cadastro_postagem, name="editar_cadastro_postagem"),
    path('update_cadastro_postagem/<int:id>', update_cadastro_postagem, name="update_cadastro_postagem"),
]
