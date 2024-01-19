from django import forms

class Cadastro(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    senha = forms.CharField(max_length=100)
    