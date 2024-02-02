from django import forms
from clientes.models import Usuario

class Entrar(forms.Form):
    email = forms.CharField(label="email", widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
