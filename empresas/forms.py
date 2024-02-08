from django import forms
from .models import PerfilLocal, Endereco

class Perfil(forms.ModelForm):
    class Meta:
        model = PerfilLocal
        fields = "__all__"
        widgets = {
            'hora_abre': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fecha': forms.TimeInput(attrs={'type': 'time'}),
            'dias_abertos': forms.CheckboxSelectMultiple(attrs={'required': False})        
            }

class Estacio(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = "__all__"

