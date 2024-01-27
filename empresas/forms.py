from django import forms

class Empresas(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.CharField(label='Email')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirme = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)
    cnpj = forms.CharField(label='CNPJ', max_length=14)