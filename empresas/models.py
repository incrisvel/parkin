from django.db import models
from main.models import Usuario

class Estacionamento(models.Model):
    nome_fantasia = models.CharField(max_length=200, blank=False, null=False, verbose_name = 'Nome')
    email = models.CharField(max_length=200, blank=False, null=False, default = '')
    razao_social = models.CharField(max_length=200, blank=False, null=False, verbose_name = 'Razão social')
    senha = models.CharField(max_length=200, default = '')
    cnpj = models.CharField(max_length=14, unique=True, blank=False, null=False, verbose_name = 'CNPJ')

    def __str__(self):
        return f"{self.nome_fantasia} - CNPJ: {self.cnpj}"
    
    
class Endereco(models.Model):
    local = models.OneToOneField(Estacionamento, on_delete=models.CASCADE)
    bairro = models.CharField(max_length=200, blank=False, null=False)
    logradouro = models.CharField(max_length=200, blank=False, null=False)
    numero = models.PositiveSmallIntegerField(blank=False, null=False)
    cep = models.CharField(max_length=10, verbose_name='CEP')
    
    
class PerfilLocal(models.Model):
    DIAS_CHOICES = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]
    local = models.OneToOneField(Estacionamento, on_delete=models.CASCADE)
    dias_abertos = models.CharField(max_length=7,choices=DIAS_CHOICES, verbose_name='dias abertos')
    hora_abre = models.TimeField
    hora_fecha = models.TimeField
    vagas_total = models.PositiveSmallIntegerField
    vagas_pref = models.PositiveSmallIntegerField
    vagas_cob = models.PositiveSmallIntegerField
    vagas_disp = models.PositiveSmallIntegerField
    descricao = models.CharField(max_length=1000, null=True, verbose_name='sobre')