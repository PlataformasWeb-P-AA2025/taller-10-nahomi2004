"""
    Manejo de urls para la aplicación
    ordenamiento
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('bienvenidos', views.index, name='index'),
        path('parroquia/<int:id>', views.obtener_parroquia, name='obtener_parroquia'),
        path('obtener_barrios', views.obtener_barrios, name='obtener_barrios'),
        path('crear/parroquia', views.crear_parroquia, name='crear_parroquia'),
        path('crear/barrio/<int:id>', views.crear_barrio_en_parroquia, name='crear_barrio_en_parroquia'),
]
