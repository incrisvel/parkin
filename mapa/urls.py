from django.urls import path
from django.contrib.auth import views as auth_views
from mapa.views import MapaView

app_name = 'mapa'

urlpatterns = [
    path('', MapaView.as_view()),
]