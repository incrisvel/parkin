from django.contrib import admin
from django.urls import path
from .views import visaogeral

urlpatterns = [
    path('/visaogeral', visaogeral, name='visaogeral')
]