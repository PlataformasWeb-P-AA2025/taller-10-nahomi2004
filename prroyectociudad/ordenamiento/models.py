from django.db import models

# Create your models here.
class Parroquia(models.Model):
	ubis = (('norte', 'norte'), ('sur', 'sur'), ('este', 'este'), ('oeste', 'oeste'))
	tipos = (('urbana', 'urbana'), ('rural', 'rural'))

	nombre = models.CharField(max_length=30)
	ubicacion = models.CharField(max_length=30, choices=ubis)
	tipo = models.CharField(max_length=30, choices=tipos)

	def __str__(self):
		return "%s %s %s" % (self.nombre,
				self.ubicacion,
				self.tipo)


class Barrio(models.Model):
	nombre = models.CharField(max_length=30)
	numero_viviendas = models.IntegerField()
	numero_parques = models.IntegerField()
	numero_edfre = models.IntegerField()
	parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name="lista_barrios")

	def __str__(self):
		return "%s %d %d %d %s" % (self.nombre,
				self.numero_viviendas,
				self.numero_parques,
				self.numero_edfre,
				self.parroquia)
