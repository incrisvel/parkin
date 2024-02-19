from django.contrib import admin
from .models import PerfilLocal

class PerfilLocalAdmin(admin.ModelAdmin):
    list_display = ['estacionamento', 'proprietarios', 'nota_media']
    readonly_fields = ['nota_media']

admin.site.register(PerfilLocal, PerfilLocalAdmin)