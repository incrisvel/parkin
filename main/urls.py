from django.contrib import admin
from django.urls import path, include
from .views import index, cadastro

urlpatterns = [
    path('', index, name='index'),
    path('cadastrar/', cadastro, name='cadastro')
]

