from django.db import models
from applications.libro.models import Libro
from .managers import PrestamoManager
from applications.autor.models import Persona


class Lector(Persona):

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo = models.DateField(auto_now=False, auto_now_add=False)
    fecha_devolucion = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    devuelto = models.BooleanField()
    objects = PrestamoManager()

    def __str__(self):
        return self.libro.titulo + ' ' + self.lector.nombre + ' ' +  self.lector.apellidos + ' ' +  str(self.lector.edad)