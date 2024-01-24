from django import forms

class Cadastro(forms.Form):
    nome = forms.CharField(label='Nome *', required = True)
    email = forms.CharField(label='Email *', required = True)
    senha = forms.CharField(label='Senha *', required = True)
    confirme = forms.CharField(label='Confirme a senha *', required = True)
    cpf = forms.CharField(label='CPF', required = True )
    datadenascimento = forms.CharField(label='Data de nascimento', required = False)
    telefone = forms.CharField(label='Telefone', required = False)
    checkbox = forms.BooleanField()