from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('video/<int:idVideo>', views.video, name="video"),
    path('videos/', views.videos, name="videos"),
    path('plataforma/<int:idPlataforma>', views.plataforma, name="plataforma"),
    path('plataformas/', views.plataformas, name="plataformas"),
    path('categoria/<int:idCategoria>', views.categoria, name="categoria"),
    path('categorias/', views.categorias, name="categorias"),
    path('contacto/', views.contacto, name="contacto"),
    ]