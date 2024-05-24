from django.urls import path
from .views import *

app_name = 'lector'

urlpatterns = [
    path('prestamo', RegistrarPrestamo.as_view(), name='prestamo_add')
]