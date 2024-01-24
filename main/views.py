from django.shortcuts import render
from .forms import Cadastro

def index(request):
    return render(request,'main/index.html')

def cadastro(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
    else:
        form = Cadastro()
        context = {
        'form' : form
        }

    return render(request, 'main/cadastro.html', context)