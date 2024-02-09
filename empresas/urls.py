from django.urls import path
from .views import resumos,  dashboard, cadastro, estacionamento, notificacao, help, comofunciona, cadastrocempresa, entrarempresa, faleconosco, fazer_logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('resumos/', resumos, name='resumos'),
    path('cadastro/', cadastro,  name='cadastro'),
    path('estacionamento/', estacionamento, name='estacionamento'),
    path('notificacoes/', notificacao, name='notificacoes'),
    path('ajuda/', help, name='ajuda'),
    path('comofunciona/', comofunciona, name='comofunciona'),
    path('cadastrar/', cadastrocempresa, name='cadastrarempresa'),
    path('entrar/', entrarempresa, name='entrarempresa'),
    path('faleconosco/', faleconosco, name='faleconosco'),
    path('logout/', fazer_logout, name='logout'),

]