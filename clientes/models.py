from django.db import models
from main.models import Usuario
from empresas.models import Estacionamento
from django.core.validators import MaxValueValidator, MinValueValidator

class Cliente(models.Model):
    nome = models.CharField(max_length=150, unique = True)
    email = models.CharField(max_length=150, unique = True, default='')
    senha = models.CharField(max_length=150, default='')
    data_nasc = models.DateField(verbose_name='data de nascimento')
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        
        
class Avaliacao(models.Model):
    avaliador = models.ForeignKey(
      Cliente, 
      on_delete=models.CASCADE, 
      related_name='cliente_avaliador', 
      verbose_name='avaliador')
    avaliado = models.ForeignKey(
      Estacionamento,
      on_delete=models.CASCADE, 
      related_name='estacionamento_avaliado', 
      verbose_name='avaliado')
    critica = models.CharField(max_length=1000, null=True, verbose_name='crítica')
    data_envio = models.DateTimeField(auto_now_add=True, verbose_name='data de envio')
    nota = models.DecimalField(max_digits=3, decimal_places=1, validators=[
                               MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return f'Avaliação de {self.avaliador} para {self.avaliado}'
        
    class Meta:
        ordering = ['data_envio']
        verbose_name ='avaliação de usuários'
        verbose_name_plural = 'avaliações de usuários'
        