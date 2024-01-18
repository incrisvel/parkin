from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50,blank=False, null=False)
    sobrenome = models.CharField(max_length=100)
    username = models.CharField(max_length=10, unique=True, null=False, blank=False, primary_key=True, verbose_name="nome de usuário")
    data_nasc = models.DateField(verbose_name="data de nascimento")
    
    def __str__(self):
        return self.nome
