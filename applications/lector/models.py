from django.db import models
from applications.libro.models import Libro
from .managers import PrestamoManager


class Lector(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
    

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo = models.DateField(auto_now=False, auto_now_add=False)
    fecha_devolucion = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    devuelto = models.BooleanField()
    prestamos = PrestamoManager()

    def __str__(self):
        return self.libro.titulo
