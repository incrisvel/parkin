from django.urls import path
from .views import cadastrocliente, entrarcliente

urlpatterns = [
    path('cadastrar/', cadastrocliente, name='cadastrocliente'),
    path('entrar/', entrarcliente, name='entrarcliente')
]

