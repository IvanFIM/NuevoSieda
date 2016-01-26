from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, Http404
from . import models
from . import forms
from .models import administradores

###### -- PORTAL SIEDA -- ######

def SiedaMain(request):
    return render(request, 'sieda/index.html' )

def Encuesta(request):
    return render(request, 'sieda/Encuesta/encuesta.html' )

###### -- PORTAL ADMINISTRATIVO -- ######
def AdminMain(request):
    admin_total = administradores.objects.count()
    return render(request, 'administrativo/index.html' , {'admin_total': admin_total})

def AdminAlta(request):
    if request.method == 'POST':
        form = forms.Administradorform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'Administrador ha sido agregado exitosamente ')
            return HttpResponseRedirect(reverse('main:admin_consultar'))
        else:
            return render(request, 'Administrativo/administradores/agregar.html', {'form': form})
    else:
        form = forms.Administradorform()
    return render(request, 'Administrativo/administradores/agregar.html', {'form': form})

def AdminEditar(request, id):
    admin = get_object_or_404(models.administradores, id=id)
    if request.method == 'POST':
        form = forms.Administradorform(request.POST, instance=admin)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Administrador ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:admin_consultar'))
        else:
            return render(request, 'Administrativo/administradores/agregar.html', {'form': form, 'admin': admin, })
    else:
        form = forms.Administradorform(instance=admin)
    return render(request, 'Administrativo/administradores/agregar.html', {'form': form, 'admin': admin, })

def AdminEliminar(request, id):
    admin = get_object_or_404(models.administradores, id=id)
    admin.delete()
    messages.add_message(request, messages.INFO, 'Administrador : {0} ha sido borrado '.format(admin.nombre))
    return HttpResponseRedirect(reverse('main:admin_consultar'))

def AdminConsultar(request):
    admin = models.administradores.objects.all()   
    return render(request, 'Administrativo/administradores/consultar.html', {'admin' : admin})
