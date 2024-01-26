from django.urls import path
from .views import index, cadastrocliente, cadastrocempresa

urlpatterns = [
    path('', index, name='index'),
    path('cadastrar/cliente/', cadastrocliente, name='cadastrocliente'),
    path('cadastrar/empresa/', cadastrocempresa, name='cadastroempresa')
]

