from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Libro


class ListaLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        f1 = self.request.GET.get('fecha1', '')
        f2 = self.request.GET.get('fecha2', '')

        if f1 and f2:
            return Libro.libros.listar_libros2(palabra_clave, f1, f2)
        else:
            return Libro.libros.listar_libros(palabra_clave)


class ListaLibros2(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista2.html'

    def get_queryset(self):
        return Libro.libros.listar_libros_categoria(2)


class LibroDetailView(DetailView):
    model = Libro
    context_object_name = 'libro'
    template_name = 'libro/detalle.html'