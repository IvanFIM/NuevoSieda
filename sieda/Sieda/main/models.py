# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser	

# Modelo para los grupos
class Grupo(models.Model):
	Grupo = models.CharField(null=True, max_length=100)
	Cuatrimestre = models.IntegerField(null=False,default=0)

	def __str__(self):
		return '{1} - {0}'.format(self.Grupo,self.Cuatrimestre)
		#return u'%s %s' % (self.Grupo, self.Cuatrimestre)
	class Meta:
		ordering = ['Cuatrimestre']

# Modelo para las carreras
class Carrera(models.Model):
	Nombre = models.CharField(null=False, max_length=100)
	Abrev_carrera = models.CharField("Abreviatura",null=False, max_length=10)

	def __unicode__(self):
		return self.Nombre
	class Meta:
		ordering = ['Nombre']

# Modelo para las materias
class Materia(models.Model):
	Nombre = models.CharField(null=False, max_length=100)
	Abrev_materia = models.CharField("Abreviatura",null=True, max_length=10)
	Grupos = models.ManyToManyField(Grupo)
	Carrera = models.ForeignKey(Carrera,null=True)

	def __unicode__(self):
		#return self.Nombre
		return u'{1} - {0}'.format(self.Nombre,self.Carrera.Abrev_carrera)

	class Meta:
		ordering = ['Carrera','Nombre']

#Modelo para maestros
class Maestro(models.Model):
	Nombre = models.CharField(null=False, max_length=100)
	Materia = models.ManyToManyField('Materia')
	Grupos = models.ManyToManyField(Grupo)

	def __unicode__(self):
		return self.Nombre

	class Meta:
		ordering = ['Nombre']


# Modelo para los jefes de carrera
class JefeCarrera(models.Model):
	Nombre = models.CharField(null=False, max_length=100)
	Carrera = models.ForeignKey(Carrera,null=True)

	def __unicode__(self):
		return self.Nombre
	class Meta:
		ordering = ['Nombre']

# Modelo para los tutores
class Tutor(models.Model):
	Maestro = models.ForeignKey(Maestro,null=True)
	Grupo = models.ForeignKey(Grupo,null=True)
	Carrera = models.ForeignKey(Carrera,null=True)

	def __unicode__(self):
		return self.Maestro.Nombre
	class Meta:
		ordering = ['Maestro']

# Modelo para preguntas
class Pregunta(models.Model):
	Descripcion = models.CharField("Descripción",null=False,max_length=600)

	def __unicode__(self):
		return self.Descripcion

	class Meta:
		ordering = ['Descripcion']


# Modelo para secciones de preguntas
class Seccion(models.Model):
	Descripcion = models.CharField("Descripción",null=False,max_length=100)
	Preguntas = models.ManyToManyField(Pregunta)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)

	def __unicode__(self):
		return self.Descripcion
	class Meta:
		ordering = ['Descripcion']

# Modelo para usuario administradores
class administradores(AbstractUser):
	Carrera = models.ForeignKey(Carrera,null=True)
	Grupo = models.ForeignKey(Grupo,null=True)
	Realizado = models.BooleanField(default=False)

# Modelo para catalogo escolar
class Catalago(models.Model):
	Descripcion = models.CharField("Descripción",null=False,max_length=100)
	Secciones = models.ManyToManyField(Seccion)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null = True, blank=True)
	EvaluacionSencilla = models.BooleanField("Evaluación sencilla",default=False)
	alumnos = models.ManyToManyField(administradores) 

	def __unicode__(self):
		return self.Descripcion
	class Meta:
		ordering = ['Descripcion']

#Modelo para periodo
class Periodo(models.Model):
	Descripcion = models.CharField(null=False,max_length=100)
	Realizado = models.BooleanField(default=False)
	Catalagos = models.ManyToManyField(Catalago)

	def __unicode__(self):
		return self.Descripcion


# Modelo para calificaciones
class Calificaciones(models.Model):
	Periodo = models.ForeignKey(Periodo,null=True)
	Seccion = models.ForeignKey(Seccion,null=True)
	Maestro = models.ForeignKey(Maestro,null=True)
	Tutor = models.ForeignKey(Tutor,null=True)
	Calificacion = models.IntegerField(null=False)
	Materia = models.ForeignKey(Materia,null=True)
	Catalogo = models.ForeignKey(Catalago,null=True)
	Grupo = models.ForeignKey(Grupo,null=True)

#Modelo para comentarios
class Comentarios(models.Model):
	Comentario = models.CharField(null=False,max_length=500)
	Alumno = models.ForeignKey(administradores,null=True)
	Catalogo = models.ForeignKey(Catalago,null=True)
	Periodo = models.ForeignKey(Periodo,null=True)

	def __str__(self):
		return self.Comentario















	

