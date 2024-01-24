from django.shortcuts import render

def dashboard(request):
    return render(request,'empresas/dashboard.html')

def resumos(request):
    return render(request,'empresas/resumos.html')

def cadastro(request):
    return render(request,'empresas/cadastro.html')