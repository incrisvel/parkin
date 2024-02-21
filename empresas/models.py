from django.db import models
from main.models import Usuario
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class EstacionamentoManager(BaseUserManager):
    def create_user(self, nome_fantasia, email, razao_social, password, cnpj):
        if not email:
            raise ValueError('O campo de e-mail é obrigatório.')
        
        novo_usuario = Usuario.objects.create(
            tipo=Usuario.Tipo.ESTACIONAMENTO,
            email=email,
            password=make_password(password)
        )  
        estacionamento = self.model(
            nome_fantasia=nome_fantasia,
            email=email,
            razao_social=razao_social,
            password=make_password(password),
            cnpj=cnpj,
            usuario = novo_usuario
        )
        estacionamento.save()
        return estacionamento

class Estacionamento(AbstractBaseUser):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='estacionamento')
    nome_fantasia = models.CharField(max_length=200, unique=True, blank=False, null=False, verbose_name='Nome Fantasia')
    email = models.EmailField(unique=True, max_length=200, blank=False, null=False)
    razao_social = models.CharField(max_length=200, blank=False, null=False, verbose_name='Razão Social')
    password = models.CharField(max_length=200, default = '')  
    cnpj = models.CharField(max_length=18, unique=True, blank=False, null=False, verbose_name='CNPJ')

    objects = EstacionamentoManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.nome_fantasia

    
class Endereco(models.Model):
    local = models.CharField(max_length=200, blank=False, null=False)
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
    dias_abertos =  models.CharField(max_length = 10, choices=DIAS_CHOICES)
    coberto = models.BooleanField(default=None)
    valor = models.FloatField(default=0)
    descricao = models.TextField(max_length = 250, verbose_name='descrição', default='')
    hora_abre = models.TimeField(default='', blank = True)
    hora_fecha = models.TimeField(default='', blank = True)
    vagas_total = models.PositiveSmallIntegerField()
    vagas_pref = models.PositiveSmallIntegerField()
    vagas_cob = models.PositiveSmallIntegerField()
    vagas_disp = models.PositiveSmallIntegerField()
    