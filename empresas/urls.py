from django.urls import path
from .views import resumos,  dashboard, cadastro, estacionamento, notificacao, help, comofunciona, cadastrocempresa, entrarempresa, faleconosco
from django.contrib.auth import views as auth_views


app_name = 'empresas'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('resumos/', resumos, name='resumos'),
    path('cadastro/', cadastro,  name='cadastro'),
    path('estacionamento/', estacionamento, name='estacionamento'),
    path('notificacoes/', notificacao, name='notificacoes'),
    path('ajuda/', help, name='ajuda'),
    path('comofunciona/', comofunciona, name='comofunciona'),
    path('cadastrar/', cadastrocempresa, name='cadastroempresa'),
    path('entrar/', entrarempresa, name='entrarempresa'),
    path('faleconosco/', faleconosco, name='faleconosco'),
]