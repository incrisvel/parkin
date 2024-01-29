from django.urls import path
from .views import index, contato
from empresas.views import dashboard, resumos, cadastro, estacionamento, notificacao, help, comofunciona, cadastrocempresa, entrarempresa

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('resumos/', resumos, name='resumos'),
    path('cadastro/', cadastro, name='cadastro'),
    path('estacionamento/', estacionamento, name='estacionamento'),
    path('notificacoes/', notificacao, name='notificacoes'),
    path('ajuda/', help, name='ajuda'),
    path('comofunciona/', comofunciona, name='comofunciona'),
    path('cadastrar/', cadastrocempresa, name='cadastrarempresa'),
    path('entrar/', entrarempresa, name='entrarempresa'),
    path('nos/',contato, name = "contato" )
]

