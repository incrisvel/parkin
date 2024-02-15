from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .forms import Perfil, Enderec
from main.views import enviar_email
from .models import Estacionamento, PerfilLocal, Endereco
from django.views.decorators.csrf import csrf_protect
from main.models import Usuario
from projeto.decorators import estacionamento_required
from django.contrib.auth import authenticate, login, logout
from projeto.backend import EmailBackend


def cadastrocempresa(request):
    erro_senha = ''
    erro_email = ''
    erro_check = ''
    erro_cnpj = ''
    
    if request.method == 'POST':
        email = request.POST.get('email')
        cnpj = request.POST.get('cnpj')
    
        if  Usuario.objects.filter(email=email).exists():
            erro_email = 'Esse email já existe!'
        
        if Estacionamento.objects.filter(cnpj=cnpj).exists():
            erro_cnpj = 'Esse CNPJ já foi registrado!'
                
        else:
            check = request.POST.get('check')
            nome_fantasia = request.POST.get('nome')
            razao_social = request.POST.get('razao')
            password = request.POST.get('senha')
            confirme = request.POST.get('senha2')

            if password == confirme and check == 'on':
                enviar_email(email)
                empresa = Estacionamento.objects.create_user(nome_fantasia=nome_fantasia, email=email, password=password, razao_social=razao_social, cnpj=cnpj)
                empresa.save()            
                return redirect('/empresas/entrar')
            if password != confirme:
                erro_senha = 'A senha não corresponde.'      
            if check != 'on':
                erro_check = 'Aceite os termos para avançar.'    
        
    return render(request, 'empresas/cadasempresa.html', {'erro_email':erro_email, 'erro_senha':erro_senha, 'erro_check':erro_check, 'erro_cnpj':erro_cnpj})

@csrf_protect
def entrarempresa(request):
    if request.user.is_authenticated:
        return render(request, 'empresas/dashboard.html')
    
    if request.method == 'POST':
        global usuario
        email = request.POST.get('email')
        senha = request.POST.get('senha')
       
        estacionamento = EmailBackend.authenticate(email=email, password=senha)

        if estacionamento is not None:   
            usuario = Estacionamento.objects.get(email=email)
            login(request, estacionamento, backend='projeto.backend.EmailBackend')
            return redirect('/empresas/dashboard')
        else:
            return redirect('/empresas/entrar')
        
    return render(request, 'empresas/entrar.html')

@estacionamento_required
def dashboard(request):
    if request.user.is_authenticated:
        usuario = Estacionamento.objects.get(email=request.user.email)
        return render(request, 'empresas/dashboard.html', {'nome': usuario.nome_fantasia})
    else:
        return render(request, 'main/acesso_negado.html')

@estacionamento_required
def fazer_logout(request):
    logout(request)
    return redirect('/')

@estacionamento_required
def resumos(request):
        return render(request,'empresas/resumos.html', {'nome': usuario.nome_fantasia})


@csrf_protect
@estacionamento_required
def cadastro(request):
    usuario = Estacionamento.objects.get(email=request.user.email)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Perfil(request.POST)
            form2 = Enderec(request.POST)
            print(form.errors)
            print(form2.errors)
            if form.is_valid() and form2.is_valid():
                perfil = form.save(commit=False)  
                endere = form2.save(commit=False)  
                perfil.proprietarios = request.user.email  
                endere.proprietarios = request.user.email  
                perfil.save() 
                endere.save() 

            return redirect('/empresas/cadastro')
        else:   
            form = Perfil()
            form2 = Enderec()
        return render(request,'empresas/cadastro.html', {'nome':usuario.nome_fantasia, 'form':form, 'form2' : form2})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def estacionamento(request):
    usuario = Estacionamento.objects.get(email=request.user.email)
    if request.user.is_authenticated:
        locais = PerfilLocal.objects.filter(proprietarios=request.user.email)
        endereco = Endereco.objects.get(proprietarios=request.user.email)
        print(endereco.local)
        return render(request,'empresas/estacionamento.html', {'nome':usuario.nome_fantasia, 'locais':locais, 'endereco':endereco})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def notificacao(request):
    if request.user.is_authenticated:
        return render(request,'empresas/notificacoes.html', {'nome':usuario.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def help(request):
    if request.user.is_authenticated:
        return render(request,'empresas/help.html', {'nome':usuario.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def comofunciona(request):
    if request.user.is_authenticated:
        return render(request,'empresas/comofunciona.html', {'nome':usuario.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

@estacionamento_required
def faleconosco(request):
    if request.user.is_authenticated:
        return render(request, 'empresas/fale_conosco.html', {'nome':usuario.nome_fantasia})
    else:
        return redirect('/empresas/entrar')
