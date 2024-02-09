from django.shortcuts import render, redirect
from main.views import enviar_email
from .models import Cliente
from django.views.decorators.csrf import csrf_protect
from main.models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password

@csrf_protect
def cadastrocliente(request):
    if request.method == 'POST':
        try:
            usuario_aux = Cliente.objects.get(email=request.POST.get('email'))
            if usuario_aux:
                return redirect('/')
        except Cliente.DoesNotExist:
            check = request.POST.get('check')
            nome_usuario = request.POST.get('nome')
            email = request.POST.get('email')
            password = request.POST.get('senha')
            confirme = request.POST.get('senha2')
            data = request.POST.get('data')
            if password == confirme and check == 'on':
                novoUsuario = Cliente.objects.create_user(nome=nome_usuario, email=email, password=password, data_nascimento=data)
                novoUsuario.save()
                return redirect('/clientes/entrar')
    return render(request, 'clientes/cadascliente.html')

@csrf_protect
def entrarcliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario_aux = Cliente.objects.filter(email=email).first()
        if email == usuario_aux.email and check_password(senha, usuario_aux.password):
            login(request, usuario_aux)
            print('Autenticado')
            return redirect('/')

        print('Não autenticado')
        return redirect('/clientes/entrar')

    return render(request, 'clientes/entrar.html')