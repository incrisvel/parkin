from django.shortcuts import render, redirect
from django.db import transaction
from main.views import enviar_email
from .models import Cliente
from django.views.decorators.csrf import csrf_protect
from main.models import Usuario
from django.contrib.auth import login
from projeto.backend import EmailBackend

@csrf_protect
def cadastrocliente(request):
    erro_senha = ''
    erro_email = ''
    erro_check = ''

    if request.method == 'POST':
        email = request.POST.get('email')
        
        if Usuario.objects.filter(email=email).exists():
            erro_email = 'Esse email já existe!'
        else:
            nome_usuario = request.POST.get('nome')
            check = request.POST.get('check')
            password = request.POST.get('senha')
            confirme = request.POST.get('senha2')
            data = request.POST.get('data')
        
            if password != confirme:
                erro_senha = 'As senhas não correspondem.'
            elif check != 'on':
                erro_check = 'Aceite os termos para avançar.'
            else:
                try:
                    with transaction.atomic():
                        cliente = Cliente.objects.create_user(nome=nome_usuario, email=email, password=password, data_nascimento=data)
                        cliente.save()
                    return redirect('/clientes/entrar')
                except Exception as e:
                    erro_email = 'Ocorreu um erro ao salvar o usuário.'
    
    return render(request, 'clientes/cadascliente.html', {'erro_email':erro_email, 'erro_senha':erro_senha, 'erro_check':erro_check})


@csrf_protect
def entrarcliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        cliente = EmailBackend.authenticate(email=email, password=senha)

        if cliente is not None and Cliente.objects.filter(email=email).exists():
            login(request, cliente, backend='projeto.backend.EmailBackend')
            return redirect('/estacionamentos/')
        else:
            return redirect('/clientes/entrar')
        
    return render(request, 'clientes/entrar.html')

