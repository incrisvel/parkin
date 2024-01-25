from django import forms

class Cadastro(forms.Form):
    nome = forms.CharField(label='Nome *')
    email = forms.CharField(label='Email *')
    senha = forms.CharField(label='Senha *', widget=forms.PasswordInput)
    confirme = forms.CharField(label='Confirme a senha *', widget=forms.PasswordInput)
    cpf = forms.CharField(label='CPF *')
    cnpj = forms.CharField(label='CNPJ *', required= False)
    datadenascimento = forms.CharField(label='Data de nascimento')
    telefone = forms.CharField(label='Telefone')