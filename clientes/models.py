from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='e-mail', unique = True)
    senha = models.
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.PositiveSmallIntegerField(choices=user_constants.USER_TYPE_CHOICES)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    def __str__(self):
      return "{}".format(self.email)

class Cliente(models.Model):
    nome = models.CharField(max_length=50,blank=False, null=False)
    sobrenome = models.CharField(max_length=100)
    username = models.CharField(max_length=10, unique=True, null=False, blank=False, primary_key=True, verbose_name='nome de usuário')
    data_nasc = models.DateField(verbose_name='data de nascimento')
    criacao_conta = models.AutoField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        
        
class Avaliacao (models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='usuario_avaliador', verbose_name='Avaliador')
    livro = models.ForeignKey(
        Livro, on_delete=models.CASCADE, related_name='livro_avaliado', verbose_name='Livro avaliado')
    dissertacao = models.CharField(max_length=1000, null=True, verbose_name='Dissertação')
    data_envio = models.DateTimeField(auto_now_add=True, verbose_name='Data de envio')
    nota = models.DecimalField(max_digits=3, decimal_places=1, validators=[
                               MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return f'Avaliação de {self.usuario} para {self.livro.titulo}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.livro.nota_media
        
    class Meta:
        ordering = ['data_envio']
        
        verbose_name ='avaliação de usuários'
        verbose_name_plural = 'avaliações de usuários'