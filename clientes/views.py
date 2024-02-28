from django.shortcuts import render, redirect
from django.db import transaction
from main.views import enviar_email
from .models import Cliente
from django.views.decorators.csrf import csrf_protect
from main.models import Usuario
from django.contrib.auth import login
from projeto.backend import EmailBackend
from datetime import datetime

def cadastrocliente(request):
    erro_senha = False
    erro_email = False
    erro_check = False
    erro_idade = False


    if request.method == 'POST':
        email = request.POST.get('email')
        email = email.lower()
    
        if Usuario.objects.filter(email=email).exists():
            erro_email = True
        else:
            nome_usuario = request.POST.get('nome')
            check = request.POST.get('check')
            password = request.POST.get('senha')
            confirme = request.POST.get('senha2')
            data = request.POST.get('data')
            data_atual = datetime.now()
            idade = data_atual.year - int(data[:4])
            if password == confirme and check == 'on':
                enviar_email(email)
                cliente = Cliente.objects.create_user(nome=nome_usuario, email=email, password=password, data_nascimento=data)
                cliente.save()
                return redirect('/clientes/entrar')
            if password != confirme:
                erro_senha = True
            if check == None:
                erro_check = True
            if idade < 18:
                erro_idade = True
                
    return render(request, 'clientes/cadascliente.html', {'erro_email':erro_email, 'erro_senha':erro_senha, 'erro_check':erro_check, 'erro_idade':erro_idade})


@csrf_protect
def entrarcliente(request):
    erro_email = False
    erro_senha = False
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        email = email.lower()

        cliente = EmailBackend.authenticate(email=email, password=senha)

        if cliente is not None and Cliente.objects.filter(email=email).exists() and Cliente.objects.filter(email=email).exists():
            login(request, cliente, backend='projeto.backend.EmailBackend')
            return redirect('/estacionamentos/')
        else:
            erro_email = True
            erro_senha = True
    return render(request, 'clientes/entrar.html', {'erro_email': erro_email, 'erro_senha':erro_senha})

