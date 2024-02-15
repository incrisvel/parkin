from django import forms
from .models import Estacionamento, PerfilLocal, Endereco

class Perfil(forms.ModelForm):
    class Meta:
        model = PerfilLocal
        fields = '__all__'
        widgets = {
            'hora_abre': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fecha': forms.TimeInput(attrs={'type': 'time'}),
            }

class Enderec(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

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
