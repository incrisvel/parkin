from django.urls import path
from .views import index, fazer_logout

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('logout/', fazer_logout, name='logout'),
]

