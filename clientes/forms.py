from django import forms
from .models import Cliente

class Usuario(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Cliente
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['data_nasc'].widget = forms.DateInput(attrs={'type':'date'})
