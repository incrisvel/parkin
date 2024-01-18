from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return f"{self.nome} - CNPJ: {self.cnpj}"
