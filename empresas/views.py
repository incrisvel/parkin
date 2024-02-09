from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .forms import Perfil, Estacio
from main.views import enviar_email
from .models import Estacionamento, PerfilLocal, Endereco
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from clientes.models import Cliente
from django.contrib.auth.hashers import check_password

nome = ''

def logado():
    global login
    if loginemp == False:
        login = False
    login = True

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
            password = request.POST.get('senha')
            confirme = request.POST.get('senha2')
            cnpj = request.POST.get('cnpj')
            if password == confirme and check == 'on':
                empresa = Estacionamento.objects.create_user(nome_fantasia=nome_fantasia, email=email, password=password, razao_social=razao_social, cnpj=cnpj)
                empresa.save()
                usuario_aux = Estacionamento.objects.filter(email=email).first()
                return redirect(reverse('dashboard') + f'?nome_fantasia={usuario_aux.nome_fantasia}&')
            return redirect('/empresas/cadastrar')
    return render(request, 'empresas/cadasempresa.html')

@csrf_protect
def entrarempresa(request):
    global usuario_aux, loginemp
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario_aux = Estacionamento.objects.filter(email=email).first()
        if email == usuario_aux.email and check_password(senha, usuario_aux.password):
            loginemp = True
            print('Autenticado')
            return redirect(reverse('dashboard') + f'?nome_fantasia={usuario_aux.nome_fantasia}&')
        print('Não autenticado')
        return redirect('/empresas/entrar')
    return render(request, 'empresas/entrar.html')

def dashboard(request):
    logado()
    if login == True:
        return render(request, 'empresas/dashboard.html', {'nome': usuario_aux.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

def fazer_logout(request):
    loginemp == False
    return redirect('/empresas/entrar')

def resumos(request):
    logado()
    if login == True:
        return render(request,'empresas/resumos.html', {'nome':nome})
    else:
        return redirect('/empresas/entrar')

def cadastro(request):
    logado()
    if login == True:
        if request.method == 'POST':
            form = Perfil(request.POST)
            form2 = Estacio(request.POST)
            print(form.errors)
            print(form2.errors)
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
        else:   
            form = Perfil()
            form2 = Estacio()
        return render(request,'empresas/cadastro.html', {'nome':nome, 'form':form, 'form2' : form2})
    else:
        return redirect('/empresas/entrar')

def estacionamento(request):
    logado()
    if login == True:
        return render(request,'empresas/estacionamento.html', {'nome':nome})
    else:
        return redirect('/empresas/entrar')


def notificacao(request):
    logado()
    if login == True:
        return render(request,'empresas/notificacoes.html', {'nome':nome})
    else:
        return redirect('/empresas/entrar')

def help(request):
    logado()
    if login == True:
        return render(request,'empresas/help.html', {'nome':nome})
    else:
        return redirect('/empresas/entrar')

def comofunciona(request):
    logado()
    if login == True:
        return render(request,'empresas/comofunciona.html', {'nome':nome})
    else:
        return redirect('/empresas/entrar')

def faleconosco(request):
    logado()
    if login == True:
        return render(request, 'empresas/fale_conosco.html', {'nome':nome})
    else:
        return redirect('/empresas/entrar')
