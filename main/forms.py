from django import forms

class Entrar(forms.Form):
    email = forms.CharField(label='Email')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)