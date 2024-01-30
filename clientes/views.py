from django.shortcuts import render, redirect
from .forms import Usuario
from main.forms import Entrar
from main.views import enviar_email

def cadastrocliente(request):
    check = 'on'
    senha = ''
    confirme = ''
    email_apparence = True
    if request.method == 'POST':
        form = Usuario(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            mail = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            confirme = request.POST.get('confirme')
            data = form.cleaned_data['data_nasc']
            check = request.POST.get('check')
            if mail.find('@') >= 1:
                email_formatado = mail.split('@')
                if email_formatado[1] == 'gmail.com' or email_formatado[1] == 'hotmail.com' or email_formatado[1] == 'outlook.com' and check != 'None' and senha == confirme:
                    enviar_email(mail)
                    form.save()
                    return redirect('/')
                elif email_formatado[1] != 'gmail.com' and email_formatado[1] != 'hotmail.com' and email_formatado[1] != 'outlook.com':
                    email_apparence = False
            else:
                email_apparence = False
                Usuario(initial={'nome':nome, 'email': mail, 'cpf':cpf, 'data':data})
    else:       
        form = Usuario()

    context = {
        'form' : form,
        'check' : check,
        'senha' : senha,
        'confirme' : confirme,
        'email_apparence' : email_apparence,
    }

    return render(request, 'clientes/cadascliente.html', context)

def entrarcliente(request):
    email_apparence = True 
    mail = ''
    senha = ''
    if request.method == 'POST':
        form = Entrar(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
    else:
        form = Entrar(initial={'email' : mail})
    context = {
        'form' : form,
        'email_apparence' : email_apparence
    }
    return render(request,'clientes/entrar.html', context)