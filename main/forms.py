from django import forms
from clientes.models import Cliente
from empresas.models import Estacionamento

class EntrarCliente(forms.Form):
    email = forms.CharField(label='Email')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        senha = cleaned_data.get('senha')
        if email and senha:
            try:
                cliente = Cliente.objects.get(email=email, senha=senha)
            except Cliente.DoesNotExist:
                raise forms.ValidationError('Email ou senha incorretos!')
            

class EntrarEstacionamento(forms.Form):
    email = forms.CharField(label='Email')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        senha = cleaned_data.get('senha')
        if email and senha:
            try:
                empresas = Estacionamento.objects.get(email=email, senha=senha)
            except Estacionamento.DoesNotExist:
                raise forms.ValidationError('Email ou senha incorretos!')