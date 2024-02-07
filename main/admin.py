from django.contrib import admin
from .models import Usuario, Feedback
from clientes.models import Cliente, Avaliacao
from empresas.models import Estacionamento, Endereco, PerfilLocal, Opcao
from django.contrib.auth.admin import UserAdmin

admin.site.register(Opcao)

@admin.register(Usuario)
class Administrador(UserAdmin):
    ordering = ['email']
    

admin.site.register(Feedback)

admin.site.register(Cliente)
admin.site.register(Avaliacao)

admin.site.register(Estacionamento)
admin.site.register(Endereco)
admin.site.register(PerfilLocal)