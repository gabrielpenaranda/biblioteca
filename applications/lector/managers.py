import datetime
from django.db import models
from django.db.models import Q, Count, Avg, Sum
from django.db.models.functions import Lower


class PrestamoManager(models.Manager):
    """ Procedimientos para prestamo """

    def libros_promedio_edades(self):
        resultado = self.aggregate(
            promedio_edad = Avg('lector__edad'),
            suma_edad = Sum('lector__edad')
        )

        return resultado

    def num_libros_prestados(self):
        resultado = self.values(
            'libro'
        ).annotate(
            num_prestados = Count('libro'),
            titulo = Lower('libro__titulo'),
        )

        for r in resultado:
            print('++++++++++++++')
            print(r, r['num_prestados'])

        return resultado

    def num_libros_devueltos(self):
        resultado = self.filter(
            devuelto = True
        ).annotate(
            num_prestados = Count('libro')
        )

        for r in resultado:
            print('++++++++++++++')
            print(r, r.num_prestados)

        return resultado