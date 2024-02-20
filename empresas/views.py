from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .forms import Estacionamento, EnderecoForm, PerfilForm
from main.views import enviar_email
from .models import Estacionamento, PerfilLocal, Endereco
from django.views.decorators.csrf import csrf_protect
from main.models import Usuario
from projeto.decorators import estacionamento_required
from django.contrib.auth import authenticate, login, logout
from projeto.backend import EmailBackend

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
    if request.method == 'POST':
        form_perfil = PerfilForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        if form_perfil.is_valid() and form_endereco.is_valid():
            perfil = form_perfil.save(commit=False)
            perfil.estacionamento = request.user.estacionamento
            perfil.save()

            endereco = form_endereco.save(commit=False)
            endereco.estacionamento = request.user.estacionamento
            endereco.save()

            return redirect('/empresas/dashboard')
    else:
        form_perfil = PerfilForm()
        form_endereco = EnderecoForm()

    return render(request, 'empresas/cadastro.html', {'form': form_perfil, 'form2': form_endereco})


@estacionamento_required
def estacionamento(request):
    usuario = Estacionamento.objects.get(email=request.user.email)
    if request.user.is_authenticated:
        locais = PerfilLocal.objects.all()
        enderecos = Endereco.objects.all()

        dias_semana = {'1': 'Segunda-feira', '2': 'Terça-feira', '3': 'Quarta-feira', '4': 'Quinta-feira', '5': 'Sexta-feira', '6': 'Sábado', '7': 'Domingo'}

        for local in locais:
            # Convertendo os dias de funcionamento de códigos para nomes de dias
            dias_abertos = [dias_semana[dia] for dia in local.dias_aberto]
            local.dias_abertos = dias_abertos  # Substituindo os códigos pelos nomes dos dias


        return render(request,'empresas/estacionamento.html', {'nome':usuario.nome_fantasia, 'locais':locais, 'enderecos':enderecos})
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