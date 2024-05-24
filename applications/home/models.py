from django.db import models


class Persona(models.Model):
    full_name = models.CharField('nombres', max_length=50, default=' ')
    pais = models.CharField('Pais', max_length=30, default=' ')
    pasaporte = models.CharField('Pasaporte', max_length=50, default=' ')
    edad = models.IntegerField(default=18)
    apelativo = models.CharField('Apelativo', max_length=10, default=' ')


    class Meta:
        # db_table = 'persona'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        unique_together = ['pais', 'apelativo']
        """
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18'),
        ]"""
        abstract = True

    def __str__(self):
        return self.full_name