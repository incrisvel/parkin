from django.shortcuts import render, redirect
from .forms import Clientes, Empresas
import smtplib
import email.message

def index(request):
    return render(request,'main/index.html')

def enviar_email():
    corpo_email = """
    <p>Paragrafo1</p>
    <p>Paragrafo2</p>
    """

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
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            confirme = form.cleaned_data['confirme']
            cpf = form.cleaned_data['cpf']
            data = form.cleaned_data['datadenascimento']
            check = request.POST.get('check')
            if email.find('@')  == True:
                email_formatado = email.split('@')
                if email_formatado[1] == 'gmail.com' or email_formatado[1] == 'hotmail.com' or email_formatado[1] ==  'outlook.com' and senha == confirme and check != 'None' and len(cpf) == 11:
                    return redirect('/')
                elif email_formatado[1] != 'gmail.com' and email_formatado[1] != 'hotmail.com' and email_formatado[1] != 'outlook.com':
                    email_apparence = False
            else:
                email_apparence = False
                Clientes(initial={'nome':nome, 'email': email, 'cpf':cpf, 'data':data})
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

    return render(request, 'main/cadascliente.html', context)


def cadastrocempresa(request):
    check = 'on'
    senha = ''
    confirme = ''
    email_apparence = True
    cnpj = '00000000000000'
    if request.method == 'POST':
        form = Empresas(request.POST)
        check = request.POST.get('check')
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            confirme = form.cleaned_data['confirme']
            cnpj = form.cleaned_data['cnpj']
            if email.find('@')  == True:
                email_formatado = email.split('@')
                if email_formatado[1] == 'gmail.com' or email_formatado[1] == 'hotmail.com' or email_formatado[1] ==  'outlook.com' and senha == confirme and check != 'None' and len(cnpj) == 14:

                    return redirect('/')
                elif email_formatado[1] != 'gmail.com' and email_formatado[1] != 'hotmail.com' and email_formatado[1] != 'outlook.com':
                    email_apparence = False
            else:
                email_apparence = False
                Empresas(initial={'nome':nome, 'email': email, 'cnpj':cnpj })
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

    return render(request, 'main/cadasempresa.html', context)