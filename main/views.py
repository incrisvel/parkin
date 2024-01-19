from django.shortcuts import render
from .forms import Cadastro

def index(request):
    return render(request,'main/index.html')

def cadastro(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
    else:
        form = Cadastro()
    context = {
        'form':form
    }
            
    return render(request, 'main/cadastro.html', context)