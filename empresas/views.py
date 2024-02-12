from django.shortcuts import render, redirect
from .forms import Perfil, Estacio
from main.views import enviar_email
from .models import Estacionamento, PerfilLocal
from django.views.decorators.csrf import csrf_protect
from main.models import Usuario
from projeto.decorators import estacionamento_required
from django.contrib.auth import authenticate, login, logout
from projeto.backend import EmailBackend

@csrf_protect
def cadastrocempresa(request):
    erro_senha = ''
    erro_email = ''
    erro_check = ''
    
    if request.method == 'POST':
        email = request.POST.get('email')
    
        if Usuario.objects.filter(email=email).exists():
            erro_email = 'Esse email já existe!'
            
        check = request.POST.get('check')
        nome_fantasia = request.POST.get('nome')
        razao_social = request.POST.get('razao')
        password = request.POST.get('senha')
        confirme = request.POST.get('senha2')
        cnpj = request.POST.get('cnpj')
    
        if password == confirme and check == 'on':
            empresa = Estacionamento.objects.create_user(nome_fantasia=nome_fantasia, email=email, password=password, razao_social=razao_social, cnpj=cnpj)
            empresa.save()            
            return redirect('/empresas/entrar')
        if password != confirme:
            erro_senha = 'A senha não corresponde.'      
        if check != 'on':
            erro_check = 'Aceite os termos para avançar.'    
        
    return render(request, 'empresas/cadasempresa.html', {'erro_email':erro_email, 'erro_senha':erro_senha, 'erro_check':erro_check})

@csrf_protect
def entrarempresa(request):
    if request.user.is_authenticated:
        return render(request, 'empresas/dashboard.html')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
       
        estacionamento = EmailBackend.authenticate(email=email, password=senha)
            
        if estacionamento is not None:   
            login(request, estacionamento)
            return redirect('/empresas/dashboard')
        else:
            return redirect('/empresas/entrar')
        
    return render(request, 'empresas/entrar.html')

@estacionamento_required
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'empresas/dashboard.html')
    else:
        return render(request, 'main/acesso_negado.html')

@estacionamento_required
def fazer_logout(request):
    logout(request)
    return redirect('/')

@estacionamento_required
def resumos(request):
        return render(request,'empresas/resumos.html', {'nome': request.user.nome_fantasia})

    
@estacionamento_required
def cadastro(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Perfil(request.POST)
            form2 = Estacio(request.POST)
            form.proprietarios = request.user
            print(request.user)
            print(form.errors)
            print(form2.errors)
            if form.is_valid() and form2.is_valid():
                perfil = form.save(commit=False)  
                perfil.proprietarios = request.user.email  
                perfil.save() 
                form2.save() 
                locais = PerfilLocal.objects.filter(proprietarios=request.user.email)
            return redirect('/empresas/cadastro')
        else:   
            locais = PerfilLocal.objects.filter(proprietarios=request.user.email)
            form = Perfil()
            form2 = Estacio()
        return render(request,'empresas/cadastro.html', {'nome':request.user.nome_fantasia, 'form':form, 'form2' : form2, 'locais':locais})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def estacionamento(request):
    if request.user.is_authenticated:
        return render(request,'empresas/estacionamento.html', {'nome':request.user.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def notificacao(request):
    if request.user.is_authenticated:
        return render(request,'empresas/notificacoes.html', {'nome':request.user.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def help(request):
    if request.user.is_authenticated:
        return render(request,'empresas/help.html', {'nome':request.user.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def comofunciona(request):
    if request.user.is_authenticated:
        return render(request,'empresas/comofunciona.html', {'nome':request.user.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def faleconosco(request):
    if request.user.is_authenticated:
        return render(request, 'empresas/fale_conosco.html', {'nome':request.user.nome_fantasia})
    else:
        return redirect('/empresas/entrar')
