# from django.urls import URLPattern

from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name = 'index'),    
    path('generales/',generales, name = 'generales'),
    path('programacion/',programacion, name = 'programacion'),
    path('tecnologia/',tecnologia, name = 'tecnologia'),
    path('videojuegos/',videojuegos, name = 'videojuegos'),
    path('<slug:slug>/',detallePost, name = 'detalle_post'),
]

