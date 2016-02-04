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
		fields = ['Nombre', 'Abrev_carrera', 'Grupos']

class Maestroform(forms.ModelForm):
	class Meta:
		model = models.Maestro
		fields = ['Nombre', 'Materia']

class Grupoform(forms.ModelForm):
	class Meta:
		model = models.Grupo
		fields = ['Cuatrimestre']

class Materiaform(forms.ModelForm):
	class Meta:
		model = models.Materia
		fields = ['Nombre']

class Tutorform(forms.ModelForm):
	class Meta:
		model = models.Tutor
		fields = ['Maestro','Grupo','Carrera']

class Periodoform(forms.ModelForm):
	class Meta:
		model = models.Periodo
		fields = ['Descripcion','Catalagos']
		widgets = {
            'Catalagos': forms.CheckboxSelectMultiple()
        }

class Catalagoform(forms.ModelForm):
	class Meta:
		model = models.Catalago
		fields = ['Descripcion','Secciones']
		widgets = {
            'Secciones': forms.CheckboxSelectMultiple()
        }

class Seccionform(forms.ModelForm):
	class Meta:
		model = models.Seccion
		fields = ['Descripcion','Preguntas']
		widgets = {
            'Preguntas': forms.CheckboxSelectMultiple()
        }

class Preguntaform(forms.ModelForm):
	class Meta:
		model = models.Pregunta
		fields = ['Descripcion']
			
		
			
		
			
		
			
		
			
		
			
		
			
				
