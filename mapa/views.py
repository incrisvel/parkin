from django.shortcuts import render
from empresas.models import PerfilLocal

def estacionamentos(request):
    locais = PerfilLocal.objects.all()

    coberto_choice = {True: 'Coberto', False: 'Não coberto'}
    for local in locais:

        coberto = coberto_choice[local.coberto]
        local.coberto = coberto


    return render(request, "mapa/estacionamentos.html", {'locais': locais})