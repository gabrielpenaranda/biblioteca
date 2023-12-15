from django.db import models
from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager


class Categoria(models.Model):
    categoria = models.CharField(max_length=30)
    objects = CategoriaManager()

    def __str__(self):
        return str(self.id) + ' - ' + self.categoria
    

class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria_libro'
        )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada', null=True, blank=True)
    visitas = models.PositiveIntegerField()
    libros = LibroManager()

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return f'{self.id}-{self.titulo}'

