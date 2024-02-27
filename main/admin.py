from django.contrib import admin
from .models import Usuario, Feedback
from clientes.models import Cliente, Avaliacao
from empresas.models import Estacionamento, Endereco
from django.contrib.auth.admin import UserAdmin


@admin.register(Usuario)
class Administrador(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'tipo', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), 
        }),
    )
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email','tipo',)
    ordering = ('email',)


admin.site.register(Feedback)

admin.site.register(Cliente)
admin.site.register(Avaliacao)

admin.site.register(Estacionamento)
admin.site.register(Endereco)
