from django.shortcuts import render, redirect
from main.views import enviar_email
from .models import Cliente
from django.views.decorators.csrf import csrf_protect
from projeto.decorators import cliente_required
from main.models import Usuario
from django.contrib.auth import login
from django.contrib.auth import login, logout
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

        nome_usuario = request.POST.get('nome')
        check = request.POST.get('check')
        password = request.POST.get('senha')
        confirme = request.POST.get('senha2')
        data = request.POST.get('data')
        
        if password == confirme and check == 'on':
            cliente = Cliente.objects.create_user(nome=nome_usuario, email=email, password=password, data_nascimento=data)
            cliente.save()
            return redirect('/clientes/entrar')
        if password != confirme:
            erro_senha = 'A senha não corresponde.'
        if check != 'on':
            erro_check = 'Aceite os termos para avançar.'    
                
    return render(request, 'clientes/cadascliente.html', {'erro_email':erro_email, 'erro_senha':erro_senha, 'erro_check':erro_check})


@csrf_protect
def entrarcliente(request):
    if request.user.is_authenticated:
        return render(request, 'main/index.html')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        cliente = EmailBackend.authenticate(email=email, password=senha)

        if cliente is not None:   
            login(request, cliente, backend='projeto.backend.EmailBackend')
            print("Autenticado")
            return redirect('/')
        else:
            print("Não autenticado")
            return redirect('/clientes/entrar')
        
    return render(request, 'clientes/entrar.html')

@cliente_required
def fazer_logout(request):
    logout(request)
    return redirect('/')
