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
  videos= get_list_or_404(Video.objects.order_by('fecha'))
  context = {'lista_videos': videos }
  return render(request, 'videos.html', context)

def plataforma(request, idPlataforma):
  plataforma= get_object_or_404(Plataforma, pk=idPlataforma)
  seleccionados=[]
  videos=get_list_or_404(Video)
  for v in videos:
    plataformas=v.plataformas.all()
    for p in plataformas:
        if p.nombre == plataforma.nombre:
            seleccionados.append(v)
  
  
  context = {'plataforma': plataforma, 'videos': seleccionados}
  return render(request, 'plataforma.html', context)

def categoria(request, idCategoria):
  categoria= get_object_or_404(Categoria, pk=idCategoria)
  seleccionados=[]
  videos=get_list_or_404(Video)
  for v in videos:
    if v.categoria.nombre == categoria.nombre:
            seleccionados.append(v)
  
  context = {'categoria': categoria, 'videos':seleccionados }
  return render(request, 'categoria.html', context)

def video(request, idVideo):
  video= get_object_or_404(Video, pk=idVideo)
  plataformasVideo=video.plataformas.all()
  seleccionados=[]
  plataformas=get_list_or_404(Plataforma)
  for p in plataformas:
    for p2 in plataformasVideo:
        if p == p2:
            seleccionados.append(p)
  context = {'video': video, 'plataformas': seleccionados}
  return render(request, 'video.html', context)

def index(request):
  categorias=get_list_or_404(Categoria)
  todosVideos= get_list_or_404(Video.objects.order_by('fecha'))
  videos=[]
  
  for c in categorias:
    actual="1970-01-01"
    video=None
    for v in todosVideos:
        if v.categoria.nombre==c.nombre and v.fecha.isoformat()>actual:
            actual=v.fecha.isoformat()
            video=v
    if video!=None:
        videos.append(video)        
  context = {'videos': videos}
  return render(request, 'index.html', context)
