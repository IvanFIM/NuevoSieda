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
       	exclude =['password','last_login','groups','is_superuser','user_permissions','is_staff','email','date_joined','is_active','Carrera','Realizado','Grupo']
        help_texts = {
            'password': _('repita la ☺contraseña'),
        }

class Alumnoform(UserCreationForm):
	class Meta:
		model = models.administradores
		fields = '__all__'
		exclude =['password','last_login','groups','is_superuser','user_permissions','email','date_joined','is_active','is_staff','Realizado']
		labels = {
			"username": _("Matricula"),
		}

class Carreraform(forms.ModelForm):
	class Meta:
		model = models.Carrera
		fields = '__all__'


class Maestroform(forms.ModelForm):
	class Meta:
		model = models.Maestro
		fields = '__all__'
		widgets = {
            'Materia': forms.CheckboxSelectMultiple()
        }

class Grupoform(forms.ModelForm):
	class Meta:
		model = models.Grupo
		fields = '__all__'

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
		fields = '__all__'
		widgets = {
            'Secciones': forms.CheckboxSelectMultiple()
        }

class Seccionform(forms.ModelForm):
	class Meta:
		model = models.Seccion
		fields = '__all__'
		widgets = {
            'Preguntas': forms.CheckboxSelectMultiple()
        }

class Preguntaform(forms.ModelForm):
	class Meta:
		model = models.Pregunta
		fields = '__all__'
			
		
class JefeCarreraform(forms.ModelForm):
	class Meta:
		model = models.JefeCarrera
		fields = '__all__'		
		
			
		
			
		
			
		
			
		
			
				
