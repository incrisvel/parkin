from django.urls import path
from .views import index, a

urlpatterns = [
    path('', index, name='index'),
    path('a/', a, name='a')
]

