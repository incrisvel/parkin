from django.db import models
from main.models import Usuario
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models import Avg
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator


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
    nome_fantasia = models.CharField(max_length=200,  blank=False, null=False, verbose_name='Nome Fantasia')
    email = models.EmailField(max_length=200, blank=False, null=False)
    razao_social = models.CharField(max_length=200, blank=False, null=False, verbose_name='Razão Social')
    password = models.CharField(max_length=200)  
    cnpj = models.CharField(max_length=18, unique=True, blank=False, null=False, verbose_name='CNPJ')

    objects = EstacionamentoManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.nome_fantasia

    
class Endereco(models.Model):
    estacionamento = models.ForeignKey(Estacionamento, on_delete=models.CASCADE, related_name='endereco')
    local = models.CharField(max_length=200, blank=False, null=False)
    bairro = models.CharField(max_length=200, blank=False, null=False)
    logradouro = models.CharField(max_length=200, blank=False, null=False)
    numero = models.PositiveSmallIntegerField(blank=False, null=False)
    cep = models.CharField(max_length=10, verbose_name='CEP')
    
    def __str__(self):
        return f'Endereço de "{self.estacionamento.nome_fantasia}"'
    
    class Meta:
        verbose_name = 'Endereço'

    
class PerfilLocal(models.Model):
    DIAS_SEMANA = (
        (1, 'Segunda-feira'),
        (2, 'Terça-feira'),
        (3, 'Quarta-feira'),
        (4, 'Quinta-feira'),
        (5, 'Sexta-feira'),
        (6, 'Sábado'),
        (7, 'Domingo')
    )

    estacionamento = models.ForeignKey(Estacionamento, on_delete=models.CASCADE, related_name='dados_perfil')
    nome_estacionamento = models.CharField(max_length = 250, verbose_name='nome_estacionamento')
    proprietarios = models.CharField(max_length = 200, null = True, blank = True)
    coberto = models.BooleanField(default = False)
    valor = models.FloatField(validators=[MinValueValidator(0.0)], verbose_name='valor (R$/h)')
    dias_aberto = MultiSelectField(choices=DIAS_SEMANA, max_choices=7, max_length=13)
    descricao = models.TextField(max_length = 250, verbose_name='descrição')
    hora_abre = models.TimeField(blank = True)
    hora_fecha = models.TimeField(blank = True)
    vagas_total = models.PositiveSmallIntegerField()
    vagas_pref = models.PositiveSmallIntegerField()
    vagas_cob = models.PositiveSmallIntegerField()
    vagas_disp = models.PositiveSmallIntegerField()
    nota_media = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], verbose_name='nota média', null=True, blank=True, editable=False)

    def update_nota_media(self):
        media = self.estacionamento_avaliado.aggregate(Avg('nota'))['nota__avg']
        self.nota_media = round(media, 1) if media else None
        self.save()
    
    def __str__(self):
        return f'Dados de "{self.estacionamento.nome_fantasia}"'
    
    class Meta:
        verbose_name_plural = 'Perfis de locais'    