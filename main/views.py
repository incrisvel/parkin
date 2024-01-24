from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')

def cadastro(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    confirme = request.POST.get('confirme')
    cpf = request.POST.get('cpf')
    cnpj = request.POST.get('cnpj')
    data = request.POST.get('data')
    telefone = request.POST.get('cell')
    check = 'on'
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirme = request.POST.get('confirme')
        cpf = request.POST.get('cpf')
        cnpj = request.POST.get('cnpj')
        data = request.POST.get('data')
        telefone = request.POST.get('cell')
        check = request.POST.get('check')
        print (email,check)

    context = {
        'email': email,
        'senha' : senha,
        'confirme' : confirme,
        'cpf' : cpf,
        'cnpj' : cnpj,
        'data' : data,
        'telefone' : telefone,
        'check' : check
    }

    return render(request, 'main/cadastro.html', context)