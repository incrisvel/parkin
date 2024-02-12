from functools import wraps
from django.shortcuts import render

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.tipo == 'ADMIN':
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'main/acesso_negado.html')
    return wrapper

def estacionamento_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.tipo == 'ESTACIONAMENTO' or request.user.tipo == 'ADMIN':
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'main/acesso_negado.html')
        else:
            return render(request, 'main/acesso_negado.html')
    return wrapper

def cliente_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.tipo == 'CLIENTE' or request.user.tipo == 'ADMIN':
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'main/acesso_negado.html')
        else:
            return render(request, 'main/acesso_negado.html')
    return wrapper