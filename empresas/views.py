from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .forms import Perfil, Estacio
from main.views import enviar_email

@csrf_protect
def cadastrocempresa(request):
    check = 'on'
    senha = ''
    confirme = ''
    email_apparence = True
    cnpj = '00000000000000'
    if request.method == 'POST':
        form = Empresas(request.POST)
        check = request.POST.get('check')
        print(form.errors)
        if form.is_valid():
            nome = form.cleaned_data['nome_fantasia']
            mail = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            confirme = request.POST.get('confirme')
            razao = form.cleaned_data['razao_social']
            cnpj = form.cleaned_data['cnpj']
            check = request.POST.get('check')
            nome_fantasia = request.POST.get('nome')
            razao_social = request.POST.get('razao')
            email = request.POST.get('email')
            password = request.POST.get('senha')
            confirme = request.POST.get('senha2')
            cnpj = request.POST.get('cnpj')
            if password == confirme and check == 'on':
                empresa = Estacionamento.objects.create_user(nome_fantasia=nome_fantasia, email=email, password=password, razao_social=razao_social, cnpj=cnpj)
                empresa.save()
                usuario_aux = Estacionamento.objects.filter(email=email).first()
                return redirect(reverse('dashboard') + f'?nome_fantasia={usuario_aux.nome_fantasia}&')
            return redirect('/empresas/cadastrar')
    return render(request, 'empresas/cadasempresa.html')

@csrf_protect
def entrarempresa(request):
    global usuario_aux, loginemp
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
    return render(request,'empresas/entrar.html', context)

def dashboard(request):
    logado()
    if login == True:
        return render(request, 'empresas/dashboard.html', {'nome': usuario_aux.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

def fazer_logout(request):
    global loginemp
    loginemp = False
    logado()
    return redirect('/empresas/entrar')

def resumos(request):
    logado()
    if login == True:
        return render(request,'empresas/resumos.html', {'nome':usuario_aux.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

def cadastro(request):
    logado()
    if login == True:
        if request.method == 'POST':
            form = Perfil(request.POST)
            form2 = Estacio(request.POST)
            print(form.errors)
            print(form2.errors)
            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
        else:   
            form = Perfil()
            form2 = Estacio()
        return render(request,'empresas/cadastro.html', {'nome':usuario_aux.nome_fantasia, 'form':form, 'form2' : form2})
    else:
        return redirect('/empresas/entrar')

def estacionamento(request):
    logado()
    if login == True:
        return render(request,'empresas/estacionamento.html', {'nome':usuario_aux.nome_fantasia})
    else:
        return redirect('/empresas/entrar')


def notificacao(request):
    logado()
    if login == True:
        return render(request,'empresas/notificacoes.html', {'nome':usuario_aux.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

def help(request):
    logado()
    if login == True:
        return render(request,'empresas/help.html', {'nome':usuario_aux.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

def comofunciona(request):
    logado()
    if login == True:
        return render(request,'empresas/comofunciona.html', {'nome':usuario_aux.nome_fantasia})
    else:
        return redirect('/empresas/entrar')

def faleconosco(request):
    logado()
    if login == True:
        return render(request, 'empresas/fale_conosco.html', {'nome':usuario_aux.nome_fantasia})
    else:
        return redirect('/empresas/entrar')
