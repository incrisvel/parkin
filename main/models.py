from django.db import models

# Create your models here.

class Usuario (models.Model):
    id = models.AutoField(primary_key=True)

class Feedback (models.Model):
    nome = models.CharField(max_length=100)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)