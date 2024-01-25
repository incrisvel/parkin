from django.shortcuts import render, redirect
from .forms import Cadastro

def index(request):
    return render(request,'main/index.html')

def cadastro(request):
    check = 'on'
    senha = ''
    confirme = ''
    if request.method == 'POST':
        form = Cadastro(request.POST)
        check = request.POST.get('check')
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            confirme = form.cleaned_data['confirme']
            cpf = form.cleaned_data['cpf']
            cnpj = form.cleaned_data['cnpj']
            data = form.cleaned_data['datadenascimento']
            telefone = form.cleaned_data['telefone']
            if senha == confirme:
                return redirect('save/')
            else:
                Cadastro(initial={'nome':nome, 'email': email, 'senha': senha, 'confirme':confirme, 'cpf':cpf, 'data':data, 'telefone':telefone})
    else:
        form = Cadastro()
    context = {
        'form' : form,
        'check' : check,
        'senha' : senha,
        'confirme' : confirme,
    }
    return render(request, 'main/cadastro.html', context)