from django import forms
from .models import Estacionamento

class Empresas(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Estacionamento
        fields = "__all__"