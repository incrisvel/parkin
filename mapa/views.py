from django.shortcuts import render


def navegar(request):
    return render(request,'mapa/navegar.html')
