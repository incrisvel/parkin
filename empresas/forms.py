from django import forms
from .models import Estacionamento, PerfilLocal, Endereco, Selecao

class Empresas(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Estacionamento
        fields = "__all__"

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
    
class Perfil(forms.ModelForm):
    class Meta:
        model = Perfillocal
        fields = "__all__"
        widgets = {
            'valor': forms.FloatField(attrs={'placeholder': 'R$'}),
            'hora_abre': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fecha': forms.TimeInput(attrs={'type': 'time'}),
            }

class Estacio(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"

