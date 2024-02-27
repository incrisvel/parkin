from django.urls import path
from mapa.views import estacionamentos, detalhe_estacionamento

app_name = 'estacionamentos'

urlpatterns = [
    path('', estacionamentos, name='estacionamentos'),
    path('detalhe_estacionamento/<int:estacionamento_id>/', detalhe_estacionamento, name='detalhe_estacionamento'),
]
