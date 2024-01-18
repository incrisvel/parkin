from django.contrib import admin
from django.urls import path, include
from .views import index
from empresas.views import visaogeral

urlpatterns = [
    path('', index, name='index'),
    path('visaogeral/', visaogeral, name='index')
]

