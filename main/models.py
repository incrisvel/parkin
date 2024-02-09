from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UsuarioManager(BaseUserManager):
  def create_user(self, email, password, **extra_fields):
      if not email:
          raise ValueError('E-mail deve ser definido')
      
      email = self.normalize_email(email)
      user = self.model(email=email, **extra_fields)
      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, password, **extra_fields):
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)
      extra_fields.setdefault('is_active', True)

      return self.create_user(email, password, **extra_fields)


class Usuario(AbstractUser):
  class Tipo(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    CLIENTE = 'CLIENTE', 'Cliente'
    ESTACIONAMENTO = 'ESTACIONAMENTO', 'Estacionamento'
  
  tipo = models.CharField(max_length=50, choices=Tipo.choices)
  username = None
  email = models.EmailField(unique=True)

  objects = UsuarioManager()
 
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['tipo'], ['email']
    
  def __str__(self):
    return "{}".format(self.email)
  
  class Meta:
        ordering = ['email']

        
class Feedback (models.Model):
  usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
  descricao = models.CharField(max_length=1000, null=False,blank=False, verbose_name='feedback')
  data_envio = models.DateTimeField(auto_now_add=True, verbose_name='data de envio')

  def __str__(self):
        return f'Comentário de {self.usuario}: {self.descricao}'
        
  class Meta:
        ordering = ['data_envio']
