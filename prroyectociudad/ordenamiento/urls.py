"""
    Manejo de urls para la aplicación
    ordenamiento
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('bienvenidos', views.index, name='index'),
        path('estudiante/<int:id>', views.obtener_estudiante,
            name='obtener_estudiante'),
        path('estudiante/busca/<str:cadena>', views.busca,
            name='busca'),
 ]
