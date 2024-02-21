from django.urls import path
from django.contrib.auth import views as auth_views
from mapa.views import estacionamentos

app_name = 'estacionamentos'

urlpatterns = [
    path('', estacionamentos, name='estacionamentos'),
]