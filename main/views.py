from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')

def cadastro(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirme = request.POST.get('confirme')
        data = request.POST.get('data')
            
    return render(request, 'main/cadastro.html')