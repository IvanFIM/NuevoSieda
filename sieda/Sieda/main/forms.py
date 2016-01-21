from django import forms
from . import models
from django.core.exceptions import ValidationError

class Administradorform(forms.ModelForm):
	class Meta:
		model = models.administradores
		fields = ['nom_user', 'nombre', 'contrasena', 'tipo']

class Alumnoform(forms.ModelForm):
	class Meta:
		model = models.Alumno
		fields = ['Matricula','Nombre','Carrera', 'Cuatrimestre', 'Contrasena' ]

class Carreraform(forms.ModelForm):
	class Meta:
		model = models.Carrera
		fields = ['Nombre', 'Abrev_carrera', 'Jefe']

class Configuracionform(forms.ModelForm):
	class Meta:
		model = models.Configuracion
		fields = ['Nombre', 'Valor']

class Grupoform(forms.ModelForm):
	class Meta:
		model = models.Grupo
		fields = ['Num_grupo', 'Carrera', 'Cuatrimestre']

class Materiaform(forms.ModelForm):
	class Meta:
		model = models.Materia
		fields = ['Nombre']

class Servicioform(forms.ModelForm):
	class Meta:
		model = models.Servicio
		fields = ['Nombre','Calificaciones']

class Tutorform(forms.ModelForm):
	class Meta:
		model = models.Tutor
		fields = ['Nombre','Num_grupo','Carrera','Cuatrimestre','Calificacion','Cantidad','Promedio']

class Periodoform(forms.ModelForm):
	class Meta:
		model = models.Periodo
		fields = ['Descripcion','Secciones']

class Seccionform(forms.ModelForm):
	class Meta:
		model = models.Seccion
		fields = ['Descripcion','Preguntas']

class Preguntaform(forms.ModelForm):
	class Meta:
		model = models.Pregunta
		fields = ['Descripcion']
			
		
			
		
			
		
			
		
			
		
			
		
			
				
