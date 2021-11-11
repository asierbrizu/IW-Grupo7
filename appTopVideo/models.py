from django.db import models
import datetime

class Plataforma(models.Model):
	nombre = models.CharField(max_length=50)
	imagen = models.CharField(max_length=100)
	empresa = models.CharField(max_length=50)
	def __str__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=100)
	edadMinima = models.IntegerField();
	def __str__(self):
		return self.nombre

class Video(models.Model):
	identificador = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)
	fecha = models.DateField(default='1970-01-01')
	descripcion = models.CharField(max_length=100)
	miniatura = models.CharField(max_length=50)
	duracion = models.IntegerField()
	calidad = models.CharField(max_length=50)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	plataformas = models.ManyToManyField(Plataforma)
	def __str__(self):
		return self.identificador

