from django.contrib import admin
from django.urls import path, include
from .views import envio_bord, home_bord

urlpatterns = [
    path('envio/', envio_bord),
    path('', home_bord),
    #path('consorcio', consorcio_bord),
]
