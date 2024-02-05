from django.contrib import admin

# coding: utf-8
from django import forms
from django.contrib import admin
from .models import *


class Mapa(forms.ModelForm):
 class Media:
  css = {
   'all': ('admin/css/geoposition_override.css',)
  }
  js = ('admin/js/geoposition_override.js',)

class MapaAdmin(admin.ModelAdmin):
 form = Mapa
 search_fields = ('endereco', 'cidade',)
 list_display = ('endereco', 'cidade','estado','bairro')
 list_filter = ['estado',]
 save_on_top = True



admin.site.register(Mapa, MapaAdmin)
