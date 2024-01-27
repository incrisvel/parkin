from django import forms

lista = list(range(2006, 1900, -1))

class Clientes(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.CharField(label='Email')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirme = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)
    cpf = forms.CharField(label='CPF', max_length=11)
    datadenascimento = forms.DateField(label = 'Data de nascimento', widget=forms.SelectDateWidget(years=lista))