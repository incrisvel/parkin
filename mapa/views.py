from django.shortcuts import render
from django.views.generic.base import (
    TemplateView,
)

class MapaView(TemplateView):
    template_name = "mapa/navegar.html"
