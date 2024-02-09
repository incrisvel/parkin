from django.db import models
from main.models import Usuario
from empresas.models import Estacionamento
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone


class ClienteManager(BaseUserManager):
    def create_user(self, nome, email, password, data_nascimento):
        if not email:
            raise ValueError('O campo de e-mail é obrigatório')
        cliente = self.model(
            nome=nome,
            email=email,
            password=make_password(password),
            data_nascimento=data_nascimento
        )
        cliente.save()
        return cliente

class Cliente(AbstractBaseUser):
    nome = models.CharField(max_length=150, unique=True)
    email = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    data_nascimento = models.DateField(null=True, blank=True)
    last_login = models.DateTimeField(default=timezone.now)  
    
    objects = ClienteManager()

    USERNAME_FIELD = 'nome'

    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome 
        
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
        