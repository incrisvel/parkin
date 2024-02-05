from django.db import models
from geoposition.fields import GeopositionField
from estados import escolha_estado

class SuaClasse(models.Model):
 """(Unidade description)"""
 endereco = models.CharField(max_length=255, verbose_name=u'Endereço', help_text='Para uma melhor localização no mapa, preencha sem abreviações. Ex: Rua Martinho Estrela,  1229') 
 bairro = models.CharField(max_length=255,)
 cidade = models.CharField(max_length=255,help_text="Para uma melhor localização no mapa, preencha sem abreviações. Ex: Belo Horizonte")
 estado = models.CharField(max_length=2, null=True, blank=True,choices=escolha_estado)
 position = GeopositionField(verbose_name=u'Geolocalização', help_text="Não altere os valores calculados automaticamente de latitude e longitude")

 class Meta:
  verbose_name, verbose_name_plural = u"Sua Classe" , u"Suas Classes"
  ordering = ('endereco',)

 def __unicode__(self):
  return u"%s" % self.endereco 
