from django.contrib import admin
from django.urls import path
from .views import dashboard, resumos, cadastro

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('resumos/', resumos, name='resumos'),
    path('cadastro/', cadastro, name='cadastro')

]