from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Carrera)
admin.site.register(models.Grupo)
admin.site.register(models.Maestro)
admin.site.register(models.Materia)
admin.site.register(models.Tutor)
admin.site.register(models.Periodo)
admin.site.register(models.Seccion)
admin.site.register(models.Pregunta)
admin.site.register(models.administradores)

