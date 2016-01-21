from django.forms import ModelForm
from . import models

class AdminForm(ModelForm):
    class Meta:
        model = models.administradores
        fields = [
            'nom_user',
            'nombre',
            'contrasena',
            'tipo',
        ]

