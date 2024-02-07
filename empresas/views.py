from django.shortcuts import render, redirect
from .forms import Empresas, Perfil, Estacio, Opcoes
from main.forms import EntrarEstacionamento
from main.views import enviar_email
from .models import Estacionamento, PerfilLocal, Endereco
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

nome = ''

@csrf_protect
def cadastrocempresa(request):
    check = 'on'
    senha = ''
    confirme = ''
    email_apparence = True
    cnpj = '00000000000000'
    if request.method == 'POST':
        form = Empresas(request.POST)
        check = request.POST.get('check')
        print(form.errors)
        if form.is_valid():
            nome = form.cleaned_data['nome_fantasia']
            mail = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            confirme = request.POST.get('confirme')
            razao = form.cleaned_data['razao_social']
            cnpj = form.cleaned_data['cnpj']
            check = request.POST.get('check')
            if mail.find('@') >= 1:
                email_formatado = mail.split('@')
                if senha == confirme and check != None and len(cnpj) == 14 and email_formatado[1] == 'gmail.com' or email_formatado[1] == 'hotmail.com' or email_formatado[1] == 'outlook.com':
                    form.save()
                    return redirect(reverse('dashboard') + f'?nome_fantasia={nome}&')
                elif email_formatado[1] != 'gmail.com' and email_formatado[1] != 'hotmail.com' and email_formatado[1] != 'outlook.com':
                    email_apparence = False
            else:
                email_apparence = False
                Empresas(initial={'nome':nome, 'email': mail, 'razao_social': razao, 'cnpj':cnpj})
    else:
        form = Empresas()
    context = {
        'form' : form,
        'check' : check,
        'senha' : senha,
        'confirme' : confirme,
        'cnpj' : len(cnpj),
        'email_apparence' : email_apparence,
    }


    return render(request, 'empresas/cadasempresa.html', context)

@csrf_protect
def entrarempresa(request):
    global nome
    email = ''
    senha = ''
    form = EntrarEstacionamento()  # Inicializa form fora do bloco de código do método POST
    if request.method == 'POST':
        form = EntrarEstacionamento(request.POST)
        print(form.errors)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            try:
                empresa = Estacionamento.objects.get(email=email, senha=senha)
                nome = empresa.nome_fantasia
                # Redireciona para o dashboard com parâmetros de consulta na URL
                return redirect(reverse('dashboard') + f'?nome_fantasia={nome}&')
            except Estacionamento.DoesNotExist:
                form.add_error(None, 'Email ou senha incorretos!')
    else:
        form = EntrarEstacionamento(initial={'email' : email}) 

    return render(request, 'empresas/entrar.html', {'form':form})

@csrf_protect
def dashboard(request):
    return render(request,'empresas/dashboard.html', {'nome':nome})

@csrf_protect
def resumos(request):
    return render(request,'empresas/resumos.html', {'nome':nome})

@csrf_protect
def cadastro(request):
    if request.method == 'POST':
        form = Perfil(request.POST)
        form2 = Estacio(request.POST)
        form3 = Opcoes(request.POST)
        print(form.errors)
        print(form2.errors)
        print(form3.errors)
        if form.is_valid() and form2.is_valid() and form3.is_valid:
            dias_abertos = form.cleaned_data['dias_abertos']
            hora_abre = form.cleaned_data['hora_abre']
            print(dias_abertos, hora_abre)
            form.save()
            form2.save()
            form3.save()
    else:   
        form = Perfil()
        form2 = Estacio()
        form3 = Opcoes()
    return render(request,'empresas/cadastro.html', {'nome':nome, 'form':form, 'form2' : form2, 'form3':form3})

@csrf_protect
def estacionamento(request):
    return render(request,'empresas/estacionamento.html', {'nome':nome})

@csrf_protect
def notificacao(request):
    return render(request,'empresas/notificacoes.html', {'nome':nome})

@csrf_protect
def help(request):
    return render(request,'empresas/help.html', {'nome':nome})

@csrf_protect
def comofunciona(request):
    return render(request,'empresas/comofunciona.html', {'nome':nome})

@csrf_protect
def faleconosco(request):
    return render(request, 'empresas/fale_conosco.html', {'nome':nome})