from django.urls import path
from .views import index, fazer_logout, fazer_logout, sobrenos, contato, paraempresas
from mapa.views import estacionamentos

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('logout/', fazer_logout, name='logout'),
    path('estacionamentos/', estacionamentos, name='estacionamentos'),
    path('sobrenos/', sobrenos, name='sobrenos'),
    path('contato/', contato, name='contato'),
    path('paraempresas/', paraempresas, name='paraempresas'),


]