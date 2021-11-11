from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404

from .models import Plataforma, Categoria, Video

#Devuelve un listado de plataformas
def plataformas(request):
  plataformas= get_list_or_404(Plataforma.objects.order_by('nombre'))
  context = {'lista_plataformas': plataformas }
  return render(request, 'plataformas.html', context)

#Devuelve un listado de categorias
def categorias(request):
  categorias= get_list_or_404(Categoria.objects.order_by('nombre'))
  context = {'lista_categorias': categorias }
  return render(request, 'categorias.html', context)

#Devuelve un listado de videos
def videos(request):
  videos= get_list_or_404(Video.objects.order_by('identificador'))
  context = {'lista_videos': videos }
  return render(request, 'videos.html', context)

def plataforma(request, nombrePlataforma):
  plataforma= get_object_or_404(Plataforma.pk==nombrePlataforma)
  context = {'plataforma': plataforma }
  return render(request, 'plataforma.html', context)

def categoria(request, nombreCategoria):
  categoria= get_object_or_404(Categoria.pk==nombreCategoria)
  context = {'categoria': categoria }
  return render(request, 'categoria.html', context)

def video(request, idVideo):
  video= get_object_or_404(Video.pk==idVideo)
  context = {'video': video }
  return render(request, 'video.html', context)

def index(request):
  return render(request, 'index.html')
def prueba(request):
  return render(request, 'base.html')
