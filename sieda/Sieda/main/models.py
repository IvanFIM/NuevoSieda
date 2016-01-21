from django.db import models

# Modelo para usuario administradores
class administradores(models.Model):
	nom_user = models.CharField(null=False, max_length=20)
	nombre = models.CharField(null=False, max_length=100)
	contrasena = models.CharField(null=False, max_length=10)
	tipo = models.CharField(null=False, max_length=20)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)
	fecha_modificacion = models.DateTimeField(auto_now=True, null = True, blank=True)

	def __str__(self):
		return self.nombre

# Modelo para alumnos
class alumnos(models.Model):
	matricula = models.IntegerField(null=False)
	nombre = models.CharField(null=False, max_length=100)
	contrasena = models.CharField(null=False, max_length=15)
	carrera = models.CharField(null=False, max_length=100)
	cuatrimestre = models.IntegerField(null=False)
	realizado = models.IntegerField(null=False,default=0)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)
	fecha_modificacion = models.DateTimeField(auto_now=True, null = True, blank=True)

	def __str__(self):
		return self.matricula

# Modelo para las carreras
class carreras(models.Model):
	nombre = models.CharField(null=False, max_length=100)
	abrev_carrera = models.CharField(null=False, max_length=10)
	jefe = models.CharField(null=False, max_length=100)

	def __str__(self):
		return self.nombre

# Modelo para la configuracion
class configuracion(models.Model):
	nombre = models.CharField(null=False, max_length=50)
	valor = models.CharField(null=False, max_length=50)

	def __str__(self):
		return self.nombre

# Modelo para los grupos
class grupos(models.Model):
	num_grupo = models.CharField(null=False, max_length=10)
	carrera = models.CharField(null=False, max_length=100)
	cuatrimestre = models.IntegerField(null=False,default=0)

	def __str__(self):
		return self.num_grupo

# Modelo para las materias
class materias(models.Model):
	nombre = models.CharField(null=False, max_length=100)

	def __str__(self):
		return self.nombre

# Modelo para los servicios
class servicios(models.Model):
	nombre = models.CharField(null=False, max_length=50)
	calificaciones = models.IntegerField(null=False,default=0)

	def __str__(self):
		return self.nombre

# Modelo para los tutores
class tutores(models.Model):
	nombre = models.CharField(null=False, max_length=100)
	num_grupo = models.CharField(null=False, max_length=10)
	carrera = models.CharField(null=False, max_length=100)
	cuatrimestre = models.IntegerField(null=False,default=0)
	calificacion = models.IntegerField(null=False,default=0)
	cantidad = models.IntegerField(null=False,default=0)
	promedio = models.IntegerField(null=False,default=0)

	def __str__(self):
		return self.nombre


	

