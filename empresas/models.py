from django.db import models
from main.models import Usuario
from django import forms
from django.utils.timezone import now


class Estacionamento(models.Model):
    nome_fantasia = models.CharField(max_length=200, unique = True, blank=False, null=False, verbose_name = 'Nome')
    email = models.CharField(max_length=200, blank=False, unique = True, null=False)
    razao_social = models.CharField(max_length=200, blank=False, null=False, verbose_name = 'Razão social')
    senha = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, unique=True, blank=False, null=False, verbose_name = 'CNPJ')

    def __str__(self):
        return f"{self.nome_fantasia} - CNPJ: {self.cnpj}"
    
    
class Endereco(models.Model):
    local = models.CharField(max_length=200, blank=False, null=False)
    bairro = models.CharField(max_length=200, blank=False, null=False)
    logradouro = models.CharField(max_length=200, blank=False, null=False)
    numero = models.PositiveSmallIntegerField(blank=False, null=False)
    cep = models.CharField(max_length=10, verbose_name='CEP')

    
class Perfillocal(models.Model):
    DIAS_CHOICES = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]
    dias_abertos =  models.CharField(max_length = 20, choices=DIAS_CHOICES)
    coberto = models.BooleanField(default=None)
    valor = models.FloatField(default=0)
    descricao = models.TextField(max_length = 250, verbose_name='descrição', default='')
    hora_abre = models.TimeField(default='', blank = True)
    hora_fecha = models.TimeField(default='', blank = True)
    vagas_total = models.PositiveSmallIntegerField()
    vagas_pref = models.PositiveSmallIntegerField()
    vagas_cob = models.PositiveSmallIntegerField()
    vagas_disp = models.PositiveSmallIntegerField()
    