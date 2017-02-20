# -*- encoding: utf-8 -*-
from django import forms
from . import models
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


class Administradorform(UserCreationForm):
    class Meta:
        model = models.administradores
        fields = '__all__'
        help_texts = {
            'password2': _('Repita la contraseña anterior.'),
        }
       	exclude =['password','last_login','groups','is_superuser','user_permissions','is_staff','email','date_joined','is_active','Carrera','Realizado','Grupo']
       

class Alumnoform(UserCreationForm):

	class Meta:
		model = models.administradores
		fields = '__all__'
		exclude =['password','password2','last_login','groups','is_superuser','user_permissions','email','date_joined','is_active','is_staff','Realizado']
		labels = {
			"username": _("Matricula"),
		}

	def clean_username(self):
		diccionario_limpio = self.cleaned_data
		username = diccionario_limpio.get('username')
		return username

	

class Carreraform(forms.ModelForm):
	class Meta:
		model = models.Carrera
		fields = '__all__'


class Maestroform(forms.ModelForm):
	class Meta:
		model = models.Maestro
		fields = '__all__'
		widgets = {
            'Materia': forms.CheckboxSelectMultiple(),
            'Grupos': forms.CheckboxSelectMultiple(),
        }


class Grupoform(forms.ModelForm):
	class Meta:
		model = models.Grupo
		fields = ['Cuatrimestre','Grupo']

class Materiaform(forms.ModelForm):
	class Meta:
		model = models.Materia
		fields = '__all__'
		widgets = {
            'Grupos': forms.CheckboxSelectMultiple()
        }

class Tutorform(forms.ModelForm):
	class Meta:
		model = models.Tutor
		fields = '__all__'

class Periodoform(forms.ModelForm):
	class Meta:
		model = models.Periodo
		fields = '__all__'
		widgets = {
            'Catalagos': forms.CheckboxSelectMultiple()
        }

class Catalagoform(forms.ModelForm):
	class Meta:
		model = models.Catalago
		fields = ['Descripcion','EvaluacionSencilla', 'Secciones']

		help_texts = {
            'Descripcion': _(u'Ingrese una dimensión'),
            'EvaluacionSencilla': _(u'Elija la opción de arriba si desea evaluar tutores, servicios, etc.'),
        }
		widgets = {
            'Secciones': forms.CheckboxSelectMultiple()
        }

class Seccionform(forms.ModelForm):
	class Meta:
		model = models.Seccion
		fields = '__all__'
		help_texts = {
            'Descripcion': _(u'Ingrese una dimensión'),
        }
		widgets = {
            'Preguntas': forms.CheckboxSelectMultiple()
        }
        
class Preguntaform(forms.ModelForm):
	class Meta:
		model = models.Pregunta
		fields = '__all__'
		help_texts = {
            'Descripcion': _('Ingrese un enunciado'),
            'Identificador': _('Ingrese el identificador de la pregunta si lo desea'),

        }

			
		
class JefeCarreraform(forms.ModelForm):
	class Meta:
		model = models.JefeCarrera
		fields = '__all__'		
		
			
		
			
		
			
		
			
		
			
				
