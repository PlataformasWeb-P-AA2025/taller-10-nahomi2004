from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *

# Create your views here.

def index(request):
	parroquias = Parroquia.objects.all()
	barrios = Barrio.objects.all()

	informacion_template = {'parroquias': parroquias, 'barrios': barrios}
	return render(request, 'index.html', informacion_template)


def obtener_barrios(request, id):
    """
        Listar los registros del modelo Barrios,
        obtenidos de la base de datos.
    """
    barrio = Barrio.objects.get(pk=id) # get: obtener un registro

    informacion_template = {'barrio': barrio}
    return render(request, 'obtener_barrio.html', informacion_template)


def busca(request, cadena):
    """
    """
    estudiantes = Estudiante.objects.filter(nombre=cadena).all()
    informacion_template = {'estudiantes': estudiantes, 'numero_estudiantes': len(estudiantes)}
    return render(request, 'busca.html', informacion_template)
