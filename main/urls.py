from django.contrib import admin
from django.urls import path, include
from .views import index
from empresas.views import dashboard, resumos, cadastro

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('resumos/', resumos, name='resumos'),
    path('cadastro/', cadastro, name='cadastro')

]

