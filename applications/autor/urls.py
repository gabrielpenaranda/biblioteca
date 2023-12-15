from django.urls import path
from .views import *

app_name = 'autor'

urlpatterns = [
    path('autores', ListAutores.as_view(), name='autores')
]