from django.urls import path
from .views import ListaLibros, ListaLibros2, LibroDetailView


app_name = 'libro'

urlpatterns = [
    path('libros/', ListaLibros.as_view(), name='libros'),
    path('libros-2/', ListaLibros2.as_view(), name='libros2'),
    path('libro-detalle/<pk>', LibroDetailView.as_view(), name='libro-detalle'),
]