from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import Perfil, Estacio
from main.views import enviar_email
from .models import Estacionamento, PerfilLocal, Endereco
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from clientes.models import Cliente

nome = ''

@csrf_protect
def cadastrocempresa(request):
    if request.method == 'POST':
        try:
            usuario_aux = Estacionamento.objects.get(email=request.POST.get('email'))
            if usuario_aux:
                return redirect('/empresas/cadastrar')

        except Estacionamento.DoesNotExist:
            check = request.POST.get('check')
            nome_fantasia = request.POST.get('nome')
            razao_social = request.POST.get('razao')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            confirme = request.POST.get('senha2')
            cnpj = request.POST.get('cnpj')
            if senha == confirme and check == 'on':
                empresa = Estacionamento.objects.create_user(nome_fantasia=nome_fantasia, email=email, password=senha, razao_social=razao_social, cnpj=cnpj)
                empresa.save()
                return redirect('/empresa/entrar')
    return render(request, 'empresas/cadasempresa.html')

@csrf_protect
def entrarempresa(request):
    global nome
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario_aux = Estacionamento.objects.filter(email=email).first()
        if usuario_aux is not None:
            usuario = authenticate(email=usuario_aux.email, password=senha)
            if usuario is not None:
                login(request, usuario)
                print('Autenticado')
                return redirect(reverse('dashboard') + f'?nome_fantasia={usuario_aux.nome_fantasia}&')
        print('Não autenticado')
        return redirect('/empresas/entrar')
    return render(request, 'empresas/entrar.html')

@login_required(login_url='/empresas/entrar')
def dashboard(request):
    try:
        estacionamento = Estacionamento.objects.get(email=request.user)
        if estacionamento.cnpj:
            return render(request, 'empresas/dashboard.html', {'nome': estacionamento.nome_fantasia})
        else:
            return redirect('/')
    except Estacionamento.DoesNotExist:
        return redirect('/')


def fazer_logout(request):
    logout(request)
    return redirect('/empresas/entrar')

@login_required(login_url='/empresas/entrar')
def resumos(request):
    return render(request,'empresas/resumos.html', {'nome':nome})

@login_required(login_url='/empresas/entrar')
def cadastro(request):
    if request.method == 'POST':
        form = Perfil(request.POST)
        form2 = Estacio(request.POST)
        print(form.errors)
        print(form2.errors)
        if form.is_valid() and form2.is_valid():
            dias_abertos = form.cleaned_data['dias_abertos']
            hora_abre = form.cleaned_data['hora_abre']
            print(dias_abertos, hora_abre)
            form.save()
            form2.save()
    else:   
        form = Perfil()
        form2 = Estacio()
    return render(request,'empresas/cadastro.html', {'nome':nome, 'form':form, 'form2' : form2})

@login_required(login_url='/empresas/entrar')
def estacionamento(request):
    return render(request,'empresas/estacionamento.html', {'nome':nome})

@login_required(login_url='/empresas/entrar')
def notificacao(request):
    return render(request,'empresas/notificacoes.html', {'nome':nome})

@login_required(login_url='/empresas/entrar')
def help(request):
    return render(request,'empresas/help.html', {'nome':nome})

@login_required(login_url='/empresas/entrar')
def comofunciona(request):
    return render(request,'empresas/comofunciona.html', {'nome':nome})

@login_required(login_url='/empresas/entrar')
def faleconosco(request):
    return render(request, 'empresas/fale_conosco.html', {'nome':nome})