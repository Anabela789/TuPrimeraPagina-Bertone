from django.urls import path
from . import views

urlpatterns = [
    # Ruta para la página principal (listado de artículos)
    path('', views.home, name='home'),
    # Ruta para crear un nuevo artículo
    path('articulo/nuevo/', views.crear_articulo, name='crear_articulo'),
    # Ruta para crear una nueva categoría
    path('categoria/nueva/', views.crear_categoria, name='crear_categoria'),
    # Ruta para crear un nuevo autor
    path('autor/nuevo/', views.crear_autor, name='crear_autor'),
    # Ruta para buscar artículos
    path('buscar/', views.buscar_articulo, name='buscar_articulo'),
]
