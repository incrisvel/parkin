from django import forms
from .models import Cliente

lista = list(range(2006, 1900, -1))


class Usuario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['data_nasc'].widget = forms.DateInput(attrs={'type':'date'})
