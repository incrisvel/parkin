from django import forms
from .models import Estacionamento, PerfilLocal, Endereco

class PerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilLocal
        widgets = {
            'hora_abre': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fecha': forms.TimeInput(attrs={'type': 'time'}),
            }
        exclude = ['estacionamento', 'endereco']


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        exclude = ['estacionamento']
