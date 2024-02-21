from django.shortcuts import render
from empresas.models import Endereco, PerfilLocal

def estacionamentos(request):
    enderecos = Endereco.objects.all()
    locais = PerfilLocal.objects.all()

    return render(request, "mapa/estacionamentos.html", {'enderecos': enderecos, 'locais': locais})

