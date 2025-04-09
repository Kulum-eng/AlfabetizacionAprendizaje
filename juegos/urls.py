from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('menu/', views.menu_juegos, name='menu_juegos'),
    path('sopa-letras/', views.sopa_letras, name='sopa_letras'),
    path('dictado/', views.dictado, name='dictado'),  
    path('palabras/', views.palabras, name='palabras')
]