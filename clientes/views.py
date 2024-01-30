from django.shortcuts import render, redirect
from .forms import Usuario
from main.forms import Entrar
from main.views import enviar_email
from django.contrib.auth.hashers import make_password, check_password
from .models import Cliente
from django.core.exceptions import ValidationError

def cadastrocliente(request):
    check = 'on'
    senha = ''
    confirme = ''
    email_apparence = True
    if request.method == 'POST':
        form = Usuario(request.POST)
        print(form.errors)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            mail = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            data = form.cleaned_data['data_nasc']
            check = request.POST.get('check')
            confirme = request.POST.get('confirme')
            if mail.find('@') >= 1:
                email_formatado = mail.split('@')
                if senha == confirme and check != None and email_formatado[1] == 'gmail.com' or email_formatado[1] == 'hotmail.com' or email_formatado[1] == 'outlook.com':
                    enviar_email(mail)
                    form.save()
                    return redirect('/')
                elif email_formatado[1] != 'gmail.com' and email_formatado[1] != 'hotmail.com' and email_formatado[1] != 'outlook.com':
                    email_apparence = False
            else:
                email_apparence = False
                Usuario(initial={'nome':nome, 'email': mail, 'data':data})
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
        print(form.errors)
        if form.is_valid():
            mail = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            try:
                cliente = Cliente.objects.get(email=mail)
            except Cliente.DoesNotExist:
                return render(request, '/a', {'erro': 'Usuário não encontrado'})

            if not check_password(senha, cliente.senha):
                return render(request, 'main/email.html', {'erro': 'Senha incorreta'})

            # Se a validação passar, você pode redirecionar para a página de sucesso ou fazer outras ações
            # Exemplo de redirecionamento:
            return redirect('/')

        return render(request, '/')
            
    else:
        form = Entrar(initial={'email' : mail})
    context = {
        'form' : form,
        'email_apparence' : email_apparence
    }
    return render(request,'clientes/entrar.html', context)