
from django.db import models


# Modelo para las categorías de los artículos
class Categoria(models.Model):
	nombre = models.CharField(max_length=100, unique=True)
	descripcion = models.TextField(blank=True)

	def __str__(self):
		return self.nombre


# Modelo para los autores de los artículos
class Autor(models.Model):
	nombre = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	bio = models.TextField(blank=True)

	def __str__(self):
		return self.nombre


# Clase base para publicaciones (herencia personalizada)
class Publicacion(models.Model):
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True  # No crea tabla, solo sirve como base

# Modelo para los artículos del blog, hereda de Publicacion
class Articulo(Publicacion):
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
	# Campo opcional para tags de grado de dificultad
	DIFICULTAD_CHOICES = [
		(None, 'Sin especificar'),
		('baja', 'Baja'),
		('media', 'Media'),
		('alta', 'Alta'),
	]
	tags = models.CharField(
		max_length=10,
		choices=DIFICULTAD_CHOICES,
		blank=True,
		null=True,
		default=None,
		help_text="Grado de dificultad (opcional)"
	)

	def __str__(self):
		return self.titulo
