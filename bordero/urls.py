from django.contrib import admin
from django.urls import path, include
from .views import envio_bord, recebido_bord

urlpatterns = [
    path('envio/', envio_bord),
    path('recebimento', recebido_bord),
]
