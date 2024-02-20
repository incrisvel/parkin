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

class Perfil(forms.ModelForm):
    class Meta:
        model = PerfilLocal
        fields = "__all__"
        widgets = {
            'hora_abre': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fecha': forms.TimeInput(attrs={'type': 'time'}),
            }

class Estacio(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"
