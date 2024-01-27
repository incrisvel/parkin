from django.shortcuts import render, redirect
from .forms import Clientes
from main.forms import Entrar
from main.views import enviar_email

def cadastrocliente(request):
    check = 'on'
    senha = ''
    confirme = ''
    email_apparence = True
    cpf = '00000000000'
    if request.method == 'POST':
        form = Clientes(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            mail = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            confirme = form.cleaned_data['confirme']
            cpf = form.cleaned_data['cpf']
            data = form.cleaned_data['datadenascimento']
            check = request.POST.get('check')
            if mail.find('@') >= 1:
                email_formatado = mail.split('@')
                print(email_formatado)
                if email_formatado[1] == 'gmail.com' or email_formatado[1] == 'hotmail.com' or email_formatado[1] ==  'outlook.com' and senha == confirme and check != 'None' and len(cpf) == 11:
                    enviar_email(mail)
                    return redirect('/')
                elif email_formatado[1] != 'gmail.com' and email_formatado[1] != 'hotmail.com' and email_formatado[1] != 'outlook.com':
                    email_apparence = False
            else:
                email_apparence = False
                Clientes(initial={'nome':nome, 'email': mail, 'cpf':cpf, 'data':data})
    else:       
        form = Clientes()
    context = {
        'form' : form,
        'check' : check,
        'senha' : senha,
        'confirme' : confirme,
        'cpf' : len(cpf),
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
            redirect ('/')
    else:
        form = Entrar(initial={'email' : mail, 'senha' : senha})
        context = {
            'form' : form,
            'email_apparence' : email_apparence
        }
    return render(request,'clientes/entrar.html', context)