from django.shortcuts import render, redirect
from .forms import Perfil, Estacio
from django.contrib.auth.decorators import permission_required
from .forms import Estacionamento
from main.views import enviar_email
from .models import Estacionamento, PerfilLocal, Endereco
from django.views.decorators.csrf import csrf_protect
from main.models import Usuario
from projeto.decorators import estacionamento_required
from django.contrib.auth import authenticate, login, logout
from projeto.backend import EmailBackend
from django.db import transaction

@csrf_protect
def cadastrocempresa(request):
    erro_senha = False
    erro_email = False
    erro_check = False
    erro_cnpj = False
    
    if request.method == 'POST':
        email = request.POST.get('email')
        cnpj = request.POST.get('cnpj')
        email = email.lower()
    
        if  Usuario.objects.filter(email=email).exists():
            erro_email = True
        if  Estacionamento.objects.filter(cnpj=cnpj).exists():
            erro_cnpj = True
            
        else:
            check = request.POST.get('check')
            nome_fantasia = request.POST.get('nome')
            razao_social = request.POST.get('razao')
            password = request.POST.get('senha')
            confirme = request.POST.get('senha2')
            cnpj = request.POST.get('cnpj')
        
            if password == confirme and check == 'on':
                empresa = Estacionamento.objects.create_user(nome_fantasia=nome_fantasia, email=email, password=password, razao_social=razao_social, cnpj=cnpj)
                empresa.save()            
                enviar_email(email)
                return redirect('/empresas/entrar')
            if password != confirme:
                erro_senha = True     
            if check == None:
                erro_check = True
        
    return render(request, 'empresas/cadasempresa.html', {'erro_email':erro_email, 'erro_senha':erro_senha, 'erro_check':erro_check, 'erro_cnpj':erro_cnpj})

@csrf_protect
def entrarempresa(request):
    erro_email = False
    erro_senha = False
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        email = email.lower()
       
        estacionamento = EmailBackend.authenticate(email=email, password=senha)

        if estacionamento is not None and Estacionamento.objects.filter(email=email).exists() and Estacionamento.objects.filter(email=email).exists():
            login(request, estacionamento, backend='projeto.backend.EmailBackend')
            return redirect('/empresas/dashboard')
        else:
            erro_email = True
            erro_senha = True
    
    return render(request, 'empresas/entrar.html', {'erro_email': erro_email, 'erro_senha':erro_senha})

@estacionamento_required
def dashboard(request):
    if request.user.is_authenticated:
        usuario = Estacionamento.objects.get(email=request.user.email)
        return render(request, 'empresas/dashboard.html', {'nome': usuario.nome_fantasia})
    else:
        return render(request, 'main/acesso_negado.html')

@estacionamento_required
def resumos(request):
    if request.user.is_authenticated:
        usuario = Estacionamento.objects.get(email=request.user.email)
        return render(request,'empresas/resumos.html', {'nome': usuario.nome_fantasia})


@csrf_protect
@estacionamento_required
def cadastro(request):
    usuario = Estacionamento.objects.get(email=request.user.email)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Perfil(request.POST)
            form2 = Estacio(request.POST)
            print(request.user.id)
            print(form.errors)
            print('------------')
            print(form2.errors)
            form.estacionemento = request.user.id
            form2.estacionemento = request.user.id
            if form.is_valid() and form2.is_valid():
                perfil = form.save(commit=False)  
                endere = form2.save(commit=False)   
                perfil.proprietarios = request.user.email
                perfil.save() 
                endere.save() 
            return redirect('/empresas/cadastro')
        else:   
            form = Perfil()
            form2 = Estacio()
        return render(request,'empresas/cadastro.html', {'nome':usuario.nome_fantasia, 'form':form, 'form2' : form2})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def estacionamento(request):
    usuario = Estacionamento.objects.get(email=request.user.email)
    if request.user.is_authenticated:
        locais = PerfilLocal.objects.filter(estacionamento=request.user.id)
        return render(request,'empresas/estacionamento.html', {'nome':usuario.nome_fantasia, 'locais':locais})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def notificacao(request):
    if request.user.is_authenticated:
        usuario = Estacionamento.objects.get(email=request.user.email)
        return render(request,'empresas/notificacoes.html', {'nome':usuario.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def help(request):
    if request.user.is_authenticated:
        usuario = Estacionamento.objects.get(email=request.user.email)
        return render(request,'empresas/help.html', {'nome':usuario.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def comofunciona(request):
    if request.user.is_authenticated:
        usuario = Estacionamento.objects.get(email=request.user.email)
        return render(request,'empresas/comofunciona.html', {'nome':usuario.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def faleconosco(request):
    if request.user.is_authenticated:
        usuario = Estacionamento.objects.get(email=request.user.email)
        return render(request, 'empresas/fale_conosco.html', {'nome':usuario.nome_fantasia})
    else:
        return redirect('/empresas/entrar')