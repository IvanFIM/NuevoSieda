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
class Alumno(models.Model):
	Matricula = models.IntegerField(null=False)
	Nombre = models.CharField(null=False, max_length=100)
	Contrasena = models.CharField(null=False, max_length=15)
	Carrera = models.CharField(null=False, max_length=100)
	Cuatrimestre = models.IntegerField(null=False)
	Realizado = models.IntegerField(null=False,default=0)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)
	fecha_modificacion = models.DateTimeField(auto_now=True, null = True, blank=True)

	def __str__(self):
		return self.Matricula

# Modelo para las carreras
class Carrera(models.Model):
	Nombre = models.CharField(null=False, max_length=100)
	Abrev_carrera = models.CharField(null=False, max_length=10)
	Jefe = models.CharField(null=False, max_length=100)

	def __str__(self):
		return self.Nombre

# Modelo para la configuracion
class Configuracion(models.Model):
	Nombre = models.CharField(null=False, max_length=50)
	Valor = models.CharField(null=False, max_length=50)

	def __str__(self):
		return self.Nombre

# Modelo para los grupos
class Grupo(models.Model):
	Num_grupo = models.CharField(null=False, max_length=10)
	Carrera = models.CharField(null=False, max_length=100)
	Cuatrimestre = models.IntegerField(null=False,default=0)

	def __str__(self):
		return self.Num_grupo

# Modelo para las materias
class Materia(models.Model):
	Nombre = models.CharField(null=False, max_length=100)

	def __str__(self):
		return self.Nombre

# Modelo para los servicios
class Servicio(models.Model):
	Nombre = models.CharField(null=False, max_length=50)
	Calificaciones = models.IntegerField(null=False,default=0)

	def __str__(self):
		return self.Nombre

# Modelo para los tutores
class Tutor(models.Model):
	Nombre = models.CharField(null=False, max_length=100)
	Num_grupo = models.CharField(null=False, max_length=10)
	Carrera = models.CharField(null=False, max_length=100)
	Cuatrimestre = models.IntegerField(null=False,default=0)
	Calificacion = models.IntegerField(null=False,default=0)
	Cantidad = models.IntegerField(null=False,default=0)
	Promedio = models.IntegerField(null=False,default=0)

	def __str__(self):
		return self.Nombre

# Modelo para preguntas
class Pregunta(models.Model):
	Descripcion = models.CharField(null=False,max_length=600)

	def __str__(self):
		self.Descripcion

# Modelo para secciones de preguntas
class Seccion(models.Model):
	Descripcion = models.CharField(null=False,max_length=100)
	Preguntas = models.ManyToManyField(Pregunta)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)

	def __str__(self):
		return self.Descripcion

# Modelo para Periodo escolar
class Periodo(models.Model):
	Descripcion = models.CharField(null=False,max_length=100)
	Secciones = models.ManyToManyField(Seccion)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)

	def __str__(self):
		return self.Descripcion









	

