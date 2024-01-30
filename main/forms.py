from django import forms
from clientes.models import Cliente

class Entrar(forms.Form):
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