from django.contrib import admin
from django.urls import path
from .views import cadastrocliente

urlpatterns = [
    path('cadastrar/', cadastrocliente, name='cadastrocliente'),
    
]

