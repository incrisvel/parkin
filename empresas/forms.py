from django import forms
from .models import Estacionamento

class Empresas(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    class Meta:
        model = Estacionamento
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['nome_fantasia'].widget.attrs['placeholder'] = 'Nome Fantasia'
        self.fields['cnpj'].widget.attrs['placeholder'] = 'CNPJ'
        self.fields['razao_social'].widget.attrs['placeholder'] = 'Razão Social'


    def clean_email(self):  
        email = self.cleaned_data['email']
        if Estacionamento.objects.filter(email=email).exists():
            print("Email já existe")
            raise forms.ValidationError('Email já cadastrado!')
        return email

    def clean_nome_fantasia(self):  
        nome_fantasia = self.cleaned_data['nome_fantasia']
        if Estacionamento.objects.filter(nome_fantasia=nome_fantasia).exists():
            print("Nome já existe")
            raise forms.ValidationError('Nome já cadastrado!')
        return nome_fantasia

    def clean_cnpj(self):  
        cnpj = self.cleaned_data['cnpj']
        if Estacionamento.objects.filter(cnpj=cnpj).exists():
            print("CNPJ já cadastrado")
            raise forms.ValidationError('CNPJ já cadastrado!')
        return cnpj