from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *
from ordenamiento.forms import *

# Create your views here.

def index(request):
	parroquias = Parroquia.objects.all()
	# barrios = Barrio.objects.all()

	informacion_template = {'parroquias': parroquias}
	return render(request, 'index.html', informacion_template)

def obtener_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    informacion_template = {'parroquia': parroquia}
    return render(request, 'obtener_parroquia.html', informacion_template)
	
def obtener_barrios(request, id):
    """
        Listar los registros del modelo Barrios,
        obtenidos de la base de datos.
    """
    barrios = Barrio.objects.all()

	informacion_template = {'barrios': barrios}
	return render(request, 'barrios.html', informacion_template)

def crear_parroquia(request):
    """
    """
    print(request)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario)

def crear_barrio_en_parroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method == 'POST':
        formulario = BarrioForm(request.POST)
        if formulario.is_valid():
            nuevo_barrio = formulario.save(commit=False)
            nuevo_barrio.parroquia = parroquia
            nuevo_barrio.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario, 'parroquia': parroquia}
    return render(request, 'crearBarrio.html', diccionario)
