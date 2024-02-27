from django.urls import path
from django.contrib.auth import views as auth_views
from mapa.views import estacionamentos, detalhe_estacionamento

app_name = 'estacionamentos'

urlpatterns = [
    path('', estacionamentos, name='estacionamentos'),
    path('<int:estacionamento_id>/', detalhe_estacionamento, name='detalhe_estacionamento'),

]