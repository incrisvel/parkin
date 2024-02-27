from django.shortcuts import render, get_object_or_404
from empresas.models import PerfilLocal

def estacionamentos(request):
    locais = PerfilLocal.objects.all()

    coberto_choice = {True: 'Coberto', False: 'Não coberto'}

    for local in locais:

        coberto = coberto_choice[local.coberto]
        local.coberto = coberto


    return render(request, "mapa/estacionamentos.html", {'locais' : locais})

def detalhe_estacionamento(request, estacionamento_id):
    
    locais = PerfilLocal.objects.all()

    coberto_choice = {True: 'Coberto', False: 'Não coberto'}
    dias_semana = {'1': 'Segunda-feira', '2': 'Terça-feira', '3': 'Quarta-feira', '4': 'Quinta-feira', '5': 'Sexta-feira', '6': 'Sábado', '7': 'Domingo'}


    for local in locais:

        coberto = coberto_choice[local.coberto]
        local.coberto = coberto
        dias_abertos = [dias_semana[dia] for dia in local.dias_aberto]
        local.dias_abertos = dias_abertos

    estacionamento = get_object_or_404(PerfilLocal, pk=estacionamento_id)
    return render(request, 'mapa/detalhe_estacionamento.html', {'estacionamento': estacionamento, 'locais': locais})