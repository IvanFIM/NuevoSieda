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

# Modelo para las materias
class Materia(models.Model):
	Nombre = models.CharField(null=False, max_length=100)

	def __str__(self):
		return self.Nombre

#Modelo para maestros
class Maestro(models.Model):
	Nombre = models.CharField(null=False, max_length=100)
	Materia = models.ManyToManyField(Materia)

	def __str__(self):
		return self.Nombre		
# Modelo para los grupos
class Grupo(models.Model):
	Cuatrimestre = models.IntegerField(null=False,default=0)

	def __int__(self):
		return self.Cuatrimestre

# Modelo para las carreras
class Carrera(models.Model):
	Nombre = models.CharField("Nombre de la carrera",null=False, max_length=100)
	Abrev_carrera = models.CharField("Abreviatura de la carrera",null=False, max_length=10)
	Grupos = models.ManyToManyField(Grupo)

	def __str__(self):
		return self.Nombre

# Modelo para los jefes de carrera
class JefeCarrera(models.Model):
	Nombre = models.CharField(null=False, max_length=100)
	Carrera = models.ForeignKey(Carrera,null=True)

	def __str__(self):
		return self.Nombre

# Modelo para alumnos
class Alumno(models.Model):
	Matricula = models.IntegerField(null=False)
	Nombre = models.CharField(null=False, max_length=100)
	Contrasena = models.CharField(null=False, max_length=15)
	Carrera = models.ForeignKey(Carrera,null=True)
	Cuatrimestre = models.IntegerField(null=False)
	Realizado = models.BooleanField(default=False)
	Grupo = models.ForeignKey(Grupo,null=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)
	fecha_modificacion = models.DateTimeField(auto_now=True, null = True, blank=True)

	def __int__(self):
		return self.Matricula

	def getCarrera(self):
		return self.Carrera.Nombre

# Modelo para los tutores
class Tutor(models.Model):
	Maestro = models.ForeignKey(Maestro,null=True)
	Grupo = models.ForeignKey(Grupo,null=True)
	Carrera = models.ForeignKey(Carrera,null=True)

	def __str__(self):
		return self.Maestro.Nombre

# Modelo para preguntas
class Pregunta(models.Model):
	Descripcion = models.CharField(null=False,max_length=600)

	def __str__(self):
		return self.Descripcion

# Modelo para secciones de preguntas
class Seccion(models.Model):
	Descripcion = models.CharField(null=False,max_length=100)
	Preguntas = models.ManyToManyField(Pregunta)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)

	def __str__(self):
		return self.Descripcion

# Modelo para catalogo escolar
class Catalago(models.Model):
	Descripcion = models.CharField(null=False,max_length=100)
	Secciones = models.ManyToManyField(Seccion)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)

	def __str__(self):
		return self.Descripcion

#Modelo para periodo
class Periodo(models.Model):
	Descripcion = models.CharField(null=False,max_length=100)
	Realizado = models.BooleanField(default=False)
	Catalagos = models.ManyToManyField(Catalago)

	def __str__(self):
		return self.Descripcion

# Modelo para calificaciones
class Calificaciones(models.Model):
	Periodo = models.ForeignKey(Periodo,null=True)
	Seccion = models.ForeignKey(Seccion,null=True)
	Maestro = models.ForeignKey(Maestro,null=True)
	Calificacion = models.IntegerField(null=False)













	

