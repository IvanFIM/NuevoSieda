from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, Http404
from . import models
from . import forms
from .models import administradores, Alumno, Carrera, Maestro, Grupo

###### -- PORTAL SIEDA -- ######

def SiedaMain(request):
    return render(request, 'sieda/index.html' )

def Encuesta(request):
    return render(request, 'sieda/Encuesta/encuesta.html' )

###### -- PORTAL ADMINISTRATIVO -- ######

def AdminMain(request):
    admin_total = administradores.objects.count()
    return render(request, 'administrativo/index.html' , {'admin_total': admin_total})

# -- ADMINISTRADORES -- 
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

# --  ALUMNOS -- 

def AlumnoAlta(request):
    if request.method == 'POST':
        form = forms.Alumnoform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'Alumno ha sido agregado exitosamente ')
            return HttpResponseRedirect(reverse('main:alumno_consultar'))
        else:
            return render(request, 'Administrativo/alumnos/agregar.html', {'form': form})
    else:
        form = forms.Alumnoform()
    return render(request, 'Administrativo/alumnos/agregar.html', {'form': form})

def AlumnoEditar(request, id):
    alumnos = get_object_or_404(models.Alumno, id=id)
    if request.method == 'POST':
        form = forms.Alumnoform(request.POST, instance=alumnos)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Alumno ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:alumno_consultar'))
        else:
            return render(request, 'Administrativo/alumnos/agregar.html', {'form': form, 'alumnos': alumnos, })
    else:
        form = forms.Alumnoform(instance=alumnos)
    return render(request, 'Administrativo/alumnos/agregar.html', {'form': form, 'alumnos': alumnos, })

def AlumnoEliminar(request, id):
    alumnos = get_object_or_404(models.Alumno, id=id)
    alumnos.delete()
    messages.add_message(request, messages.INFO, 'Alumno : {0} ha sido borrado '.format(alumnos.Nombre))
    return HttpResponseRedirect(reverse('main:alumno_consultar'))

def AlumnoConsultar(request):
    alumnos = models.Alumno.objects.all() 
    return render(request, 'Administrativo/alumnos/consultar.html', {'alumnos' : alumnos})

# --  CARRERAS -- 

def CarreraAlta(request):
    if request.method == 'POST':
        form = forms.Carreraform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'Alumno ha sido agregado exitosamente ')
            return HttpResponseRedirect(reverse('main:carrera_consultar'))
        else:
            return render(request, 'Administrativo/carreras/agregar.html', {'form': form})
    else:
        form = forms.Carreraform()
    return render(request, 'Administrativo/carreras/agregar.html', {'form': form})

def CarreraEditar(request, id):
    carreras = get_object_or_404(models.Carrera, id=id)
    if request.method == 'POST':
        form = forms.Carreraform(request.POST, instance=carreras)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Carrera ha sido modificada exitosamente ')
            return HttpResponseRedirect(reverse('main:carrera_consultar'))
        else:
            return render(request, 'Administrativo/carreras/agregar.html', {'form': form, 'carreras': carreras, })
    else:
        form = forms.Carreraform(instance=carreras)
    return render(request, 'Administrativo/carreras/agregar.html', {'form': form, 'carreras': carreras, })

def CarreraEliminar(request, id):
    carreras = get_object_or_404(models.Carrera, id=id)
    carreras.delete()
    messages.add_message(request, messages.INFO, 'Carrera : {0} ha sido borrada '.format(carreras.Nombre))
    return HttpResponseRedirect(reverse('main:carrera_consultar'))

def CarreraConsultar(request):
    carreras = models.Carrera.objects.all()   
    return render(request, 'Administrativo/carreras/consultar.html', {'carreras' : carreras})


# --  MAESTROS -- 

def MaestroAlta(request):
    if request.method == 'POST':
        form = forms.Maestroform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'Maestro ha sido agregado exitosamente ')
            return HttpResponseRedirect(reverse('main:maestro_consultar'))
        else:
            return render(request, 'Administrativo/maestros/agregar.html', {'form': form})
    else:
        form = forms.Maestroform()
    return render(request, 'Administrativo/maestros/agregar.html', {'form': form})

def MaestroEditar(request, id):
    maestros = get_object_or_404(models.Maestro, id=id)
    if request.method == 'POST':
        form = forms.Maestroform(request.POST, instance=maestros)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Maestro ha sido modificada exitosamente ')
            return HttpResponseRedirect(reverse('main:maestro_consultar'))
        else:
            return render(request, 'Administrativo/maestros/agregar.html', {'form': form, 'maestros': maestros, })
    else:
        form = forms.Maestroform(instance=maestros)
    return render(request, 'Administrativo/maestros/agregar.html', {'form': form, 'maestros': maestros, })

def MaestroEliminar(request, id):
    maestros = get_object_or_404(models.Maestro, id=id)
    maestros.delete()
    messages.add_message(request, messages.INFO, 'Maestro : {0} ha sido borrada '.format(maestros.Nombre))
    return HttpResponseRedirect(reverse('main:maestro_consultar'))

def MaestroConsultar(request):
    maestros = models.Maestro.objects.all()   
    return render(request, 'Administrativo/maestros/consultar.html', {'maestros' : maestros})

# --  GRUPOS -- 

def GrupoAlta(request):
    if request.method == 'POST':
        form = forms.Grupoform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'Grupo ha sido agregado exitosamente ')
            return HttpResponseRedirect(reverse('main:grupo_consultar'))
        else:
            return render(request, 'Administrativo/grupos/agregar.html', {'form': form})
    else:
        form = forms.Grupoform()
    return render(request, 'Administrativo/grupos/agregar.html', {'form': form})

def GrupoEditar(request, id):
    grupos = get_object_or_404(models.Grupo, id=id)
    if request.method == 'POST':
        form = forms.Grupoform(request.POST, instance=grupos)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Grupo ha sido modificada exitosamente ')
            return HttpResponseRedirect(reverse('main:Grupo_consultar'))
        else:
            return render(request, 'Administrativo/grupos/agregar.html', {'form': form, 'grupos': grupos, })
    else:
        form = forms.Grupoform(instance=grupos)
    return render(request, 'Administrativo/grupos/agregar.html', {'form': form, 'grupos': grupos, })

def GrupoEliminar(request, id):
    grupos = get_object_or_404(models.Grupo, id=id)
    grupos.delete()
    messages.add_message(request, messages.INFO, 'Grupo : {0} ha sido borrada '.format(grupos.nombre))
    return HttpResponseRedirect(reverse('main:grupo_consultar'))

def GrupoConsultar(request):
    grupos = models.Grupo.objects.all()   
    return render(request, 'Administrativo/grupos/consultar.html', {'grupos' : grupos})

    # --  CATALOGO -- 

def CatalogoAlta(request):
    if request.method == 'POST':
        form = forms.Catalagoform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'Catalago ha sido agregado exitosamente ')
            return HttpResponseRedirect(reverse('main:catalogo_consultar'))
        else:
            return render(request, 'Administrativo/Catalogo/agregar.html', {'form': form})
    else:
        form = forms.Catalagoform()
    return render(request, 'Administrativo/Catalogo/agregar.html', {'form': form})

def CatalogoEditar(request, id):
    catalago = get_object_or_404(models.Catalago, id=id)
    if request.method == 'POST':
        form = forms.Catalagoform(request.POST, instance=catalago)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Catalago ha sido modificada exitosamente ')
            return HttpResponseRedirect(reverse('main:catalogo_consultar'))
        else:
            return render(request, 'Administrativo/Catalogo/agregar.html', {'form': form, 'catalago': catalago, })
    else:
        form = forms.Catalagoform(instance=catalago)
    return render(request, 'Administrativo/Catalogo/agregar.html', {'form': form, 'catalago': catalago, })

def CatalogoEliminar(request, id):
    catalago = get_object_or_404(models.Catalago, id=id)
    catalago.delete()
    messages.add_message(request, messages.INFO, 'Catalago : {0} ha sido borrada '.format(catalago.Descripcion))
    return HttpResponseRedirect(reverse('main:catalogo_consultar'))

def CatalogoConsultar(request):
    catalago = models.Catalago.objects.all()   
    return render(request, 'Administrativo/Catalogo/consultar.html', {'catalago' : catalago})

    # --  PERIODO -- 

def PeriodoAlta(request):
    if request.method == 'POST':
        form = forms.Periodoform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'Periodo ha sido agregado exitosamente ')
            return HttpResponseRedirect(reverse('main:periodo_consultar'))
        else:
            return render(request, 'Administrativo/Periodo/agregar.html', {'form': form})
    else:
        form = forms.Periodoform()
    return render(request, 'Administrativo/Periodo/agregar.html', {'form': form})

def PeriodoEditar(request, id):
    periodo = get_object_or_404(models.Periodo, id=id)
    if request.method == 'POST':
        form = forms.Periodoform(request.POST, instance=periodo)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Periodo ha sido modificada exitosamente ')
            return HttpResponseRedirect(reverse('main:periodo_consultar'))
        else:
            return render(request, 'Administrativo/Periodo/agregar.html', {'form': form, 'catalago': catalago, })
    else:
        form = forms.Periodoform(instance=periodo)
    return render(request, 'Administrativo/Periodo/agregar.html', {'form': form, 'periodo': periodo, })

def PeriodoEliminar(request, id):
    periodo = get_object_or_404(models.Periodo, id=id)
    periodo.delete()
    messages.add_message(request, messages.INFO, 'Periodo : {0} ha sido borrada '.format(periodo.Descripcion))
    return HttpResponseRedirect(reverse('main:periodo_consultar'))

def PeriodoConsultar(request):
    periodo = models.Periodo.objects.all()   
    return render(request, 'Administrativo/Periodo/consultar.html', {'periodo' : periodo})

    # --  SECCION -- 

def SeccionAlta(request):
    if request.method == 'POST':
        form = forms.Seccionform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'Seccion ha sido agregado exitosamente ')
            return HttpResponseRedirect(reverse('main:seccion_consultar'))
        else:
            return render(request, 'Administrativo/Seccion/agregar.html', {'form': form})
    else:
        form = forms.Seccionform()
    return render(request, 'Administrativo/Seccion/agregar.html', {'form': form})

def SeccionEditar(request, id):
    seccion = get_object_or_404(models.Seccion, id=id)
    if request.method == 'POST':
        form = forms.Seccionform(request.POST, instance=seccion)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Seccion ha sido modificada exitosamente ')
            return HttpResponseRedirect(reverse('main:seccion_consultar'))
        else:
            return render(request, 'Administrativo/Seccion/agregar.html', {'form': form, 'seccion': seccion, })
    else:
        form = forms.Seccionform(instance=seccion)
    return render(request, 'Administrativo/Periodo/agregar.html', {'form': form, 'seccion': seccion, })

def SeccionEliminar(request, id):
    seccion = get_object_or_404(models.Seccion, id=id)
    seccion.delete()
    messages.add_message(request, messages.INFO, 'Seccion : {0} ha sido borrada '.format(seccion.Descripcion))
    return HttpResponseRedirect(reverse('main:seccion_consultar'))

def SeccionConsultar(request):
    seccion = models.Seccion.objects.all()   
    return render(request, 'Administrativo/Seccion/consultar.html', {'seccion' : seccion})

    # --  PREGUNTA -- 

def PreguntaAlta(request):
    if request.method == 'POST':
        form = forms.Preguntaform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'Pregunta ha sido agregado exitosamente ')
            return HttpResponseRedirect(reverse('main:pregunta_consultar'))
        else:
            return render(request, 'Administrativo/Pregunta/agregar.html', {'form': form})
    else:
        form = forms.Preguntaform()
    return render(request, 'Administrativo/Pregunta/agregar.html', {'form': form})

def PreguntaEditar(request, id):
    pregunta = get_object_or_404(models.Pregunta, id=id)
    if request.method == 'POST':
        form = forms.Preguntaform(request.POST, instance=pregunta)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'Pregunta ha sido modificada exitosamente ')
            return HttpResponseRedirect(reverse('main:pregunta_consultar'))
        else:
            return render(request, 'Administrativo/Pregunta/agregar.html', {'form': form, 'pregunta': pregunta, })
    else:
        form = forms.Preguntaform(instance=pregunta)
    return render(request, 'Administrativo/Pregunta/agregar.html', {'form': form, 'pregunta': pregunta, })

def PreguntaEliminar(request, id):
    pregunta = get_object_or_404(models.Pregunta, id=id)
    pregunta.delete()
    messages.add_message(request, messages.INFO, 'Pregunta : {0} ha sido borrada '.format(pregunta.Descripcion))
    return HttpResponseRedirect(reverse('main:pregunta_consultar'))

def PreguntaConsultar(request):
    pregunta = models.Pregunta.objects.all()   
    return render(request, 'Administrativo/Pregunta/consultar.html', {'pregunta' : pregunta})

#  --Evaluacion--
def CatalogoPreguntas(request):
    periodo = models.Periodo.objects.filter(Realizado=False)
    catalago = periodo.Catalagos.all()[0]
    seccion = catalago.Secciones.all()[0]
    return render(request, 'sieda/Evaluacion/consultar.html', {'seccion' : seccion, 'preguntas' : seccion.Preguntas})

