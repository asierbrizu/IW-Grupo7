from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('video/<str:idVideo>', views.video, name="video"),
    path('videos/', views.videos, name="videos"),
    path('plataforma/<str:nombrePlataforma>', views.plataforma, name="plataforma"),
    path('plataformas/', views.plataformas, name="plataformas"),
    path('categoria/<str:nombreCategoria>', views.categoria, name="categoria"),
    path('categorias/', views.categorias, name="categorias"),
  
    path('prueba/', views.prueba, name="prueba"),
    ]