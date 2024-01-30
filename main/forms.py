from django import forms
from clientes.models import Usuario

class Entrar(forms.Form):
    email = forms.CharField(label='Email')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
