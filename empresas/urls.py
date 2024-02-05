from django.urls import path
from .views import dashboard, resumos, cadastro, estacionamento, notificacao, help, comofunciona, cadastrocempresa, entrarempresa, cadastroestacionamento, faleconosco

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('resumos/', resumos, name='resumos'),
    path('cadastro/', cadastro, name='cadastro'),
    path('estacionamento/', estacionamento, name='estacionamento'),
    path('notificacoes/', notificacao, name='notificacoes'),
    path('ajuda/', help, name='ajuda'),
    path('comofunciona/', comofunciona, name='comofunciona'),
    path('cadastrar/', cadastrocempresa, name='cadastrarempresa'),
    path('entrar/', entrarempresa, name='entrarempresa'),
    path('cadastroestacionamento/', cadastroestacionamento, name='cadastro_estacionamento'),
    path('faleconosco/', faleconosco, name='faleconosco'),

]