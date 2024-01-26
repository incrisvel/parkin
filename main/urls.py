from django.contrib import admin
from django.urls import path, include
from .views import index
from empresas.views import dashboard, resumos, cadastro, estacionamento, notificacao, help, comofunciona

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('resumos/', resumos, name='resumos'),
    path('cadastro/', cadastro, name='cadastro'),
    path('estacionamento/', estacionamento, name='estacionamento'),
    path('notificacoes/', notificacao, name='notificacoes'),
    path('ajuda/', help, name='ajuda'),
    path('comofunciona/', comofunciona, name='comofunciona')


]

