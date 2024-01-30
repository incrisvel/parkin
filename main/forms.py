from django import forms
from clientes.models import Usuario

class Entrar(forms.Form):
    email = forms.CharField(label='Email')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    def clean_email_validation(self):  
        email = self.cleaned_data['email']
        if Usuario.objects.filter(email=email).exists():
            print("Email existe")
            email_valido = True
        else:
            print("Email não existe")
            email_valido = False
        return email_valido