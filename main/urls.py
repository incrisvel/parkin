from django.urls import path
from .views import index, fazer_logout, fazer_logout, quemsomos
from mapa.views import MapaView

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('logout/', fazer_logout, name='logout'),
    path('estacionamentos/', MapaView.as_view(), name='estacionamentos'),
    path('quemsomos/', quemsomos, name='quemsomos')
]
