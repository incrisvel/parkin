from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin

admin.site.register(Usuario)

@admin.register(Usuario)
class Administrador(UserAdmin):
    pass