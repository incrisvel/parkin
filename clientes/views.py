from django.shortcuts import render, redirect
from main.views import enviar_email
from .models import Cliente
from django.views.decorators.csrf import csrf_protect
from main.models import Usuario
from django.contrib.auth import authenticate, login, logout

@csrf_protect
def cadastrocliente(request):
    if request.method == 'POST':
        try:
            usuario_aux = Cliente.objects.get(email=request.POST.get('email'))
            if usuario_aux:
                return render(request, 'clientes/inicialcliente.html', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})

        except Cliente.DoesNotExist:
            tipo = 'CLIENTE'
            check = request.POST.get('check')
            nome_usuario = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            confirme = request.POST.get('senha2')
            if senha == confirme and check == 'on':
                novoUsuario = Cliente.objects.create_user(username=nome_usuario, email=email, password=senha)
                novoUsuario.save()
                return redirect('/clientes/entrar')
    return render(request, 'clientes/cadascliente.html')

@csrf_protect
def entrarcliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario_aux = Cliente.objects.filter(email=email).first()
        if usuario_aux is not None:
            usuario = authenticate(email=usuario_aux.email, password=senha)
            if usuario is not None:
                login(request, usuario)
                print('Autenticado')
                return redirect('/')
        
        print('Não autenticado')
        return redirect('/clientes/entrar')

    return render(request, 'clientes/entrar.html')