from django.shortcuts import render, get_object_or_404, redirect
from empresas.models import PerfilLocal
from .forms import AvaliacaoForm
from django.contrib.auth.decorators import login_required



def estacionamentos(request):
    locais = PerfilLocal.objects.all()

    coberto_choice = {True: 'Coberto', False: 'Não coberto'}

    for local in locais:

        coberto = coberto_choice[local.coberto]
        local.coberto = coberto


    return render(request, "mapa/estacionamentos.html", {'locais' : locais})

def detalhe_estacionamento(request, estacionamento_id):
    estacionamento = get_object_or_404(PerfilLocal, pk=estacionamento_id)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.avaliador = request.user.cliente
            avaliacao.avaliado = estacionamento
            avaliacao.save()
            return redirect('estacionamentos:detalhe_estacionamento', estacionamento_id=estacionamento_id)
    else:
        form = AvaliacaoForm()
    
    coberto_choice = {True: 'Coberto', False: 'Não coberto'}
    dias_semana = {'1': 'Segunda-feira', '2': 'Terça-feira', '3': 'Quarta-feira', '4': 'Quinta-feira', '5': 'Sexta-feira', '6': 'Sábado', '7': 'Domingo'}

    estacionamento.coberto = coberto_choice[estacionamento.coberto]

    dias_abertos = [dias_semana[dia] for dia in estacionamento.dias_aberto]
    estacionamento.dias_abertos = dias_abertos
    

    return render(request, 'mapa/detalhe_estacionamento.html', {'estacionamento': estacionamento, 'form': form})