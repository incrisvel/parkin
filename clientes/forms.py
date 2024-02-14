from django import forms
from .models import Cliente

class Usuario(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    class Meta:
        model = Cliente
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['data_nasc'].widget = forms.DateInput(attrs={'type': 'date', 'placeholder': 'Data de Nascimento'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['nome'].widget.attrs.update({'placeholder': 'Nome'})
    
    def clean_email(self):  
        email = self.cleaned_data['email']
        if Cliente.objects.filter(email=email).exists():
            print("Email já existe")
            raise forms.ValidationError('Email já cadastrado!')
        return email
    
    def clean_nome(self):   
        nome = self.cleaned_data['nome']
        if Cliente.objects.filter(nome=nome).exists():
            print("Nome já existe")
            raise forms.ValidationError('Nome já cadastrado!')
        return nome
