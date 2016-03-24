# -*- encoding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.db.models.functions import Lower
from django.template import loader
from . import models
from . import forms
from .models import administradores, Alumno, Carrera, Maestro, Grupo, Tutor, JefeCarrera, Materia, Seccion
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

def Error(request):
    return render(request, 'error.html' )

def Cerrar(request):
    return render(request, 'cerrar.html' )

###### -- PORTAL SIEDA -- ######

def SiedaMain(request):
    return render(request, 'sieda/login.html' )

#@login_required(login_url='/')
def Evaluacion(request):
    per = models.Periodo.objects.filter(Realizado=False)

    return render(request, 'sieda/Evaluacion/index.html', {'per' :per })

def Evaluacion_sencilla(request,id):
    per = models.Periodo.objects.filter(Realizado=False)
    cat = per[0].Catalagos.get(id=id)
    seccion = cat.Secciones.all()[0]
    pregunta = seccion.Preguntas.all()



    return render(request, 'sieda/Evaluacion/Evaluacion_sencilla.html', {'seccion' :seccion ,'preguntas':pregunta, 'catalogo': cat})


def Fin(request):
    return render(request, 'sieda/Evaluacion/fin.html')



###### -- PORTAL ADMINISTRATIVO -- ######
@login_required(login_url='/')
def AdminMain(request):
    if not request.user.is_staff:
        return render(request, 'sieda/Evaluacion/index.html')
    maestros_total = Maestro.objects.count()
    alumnos_total = administradores.objects.filter(is_staff=False).count()
    carreras_total = Carrera.objects.count()
    tutores_total = Tutor.objects.count()
    alumnos_faltantes = administradores.objects.filter(is_staff=False).filter(Realizado=False).count()


    return render(request, 'administrativo/index.html' , {'tutores_total': tutores_total, 
        'alumnos_total':alumnos_total, 'carreras_total':carreras_total, 'alumnos_faltantes':alumnos_faltantes,})

# -- ADMINISTRADORES -- 
def AdminAlta(request):
    if request.method == 'POST':
        form = forms.Administradorform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_staff = True
            instance.is_superuser = True
            instance.save()
            messages.add_message(request, messages.INFO, 'El administrador ha sido agregado exitosamente ')
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
            messages.add_message(request, messages.INFO, 'El administrador ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:admin_consultar'))
        else:
            return render(request, 'Administrativo/administradores/agregar.html', {'form': form, 'admin': admin, })
    else:
        form = forms.Administradorform(instance=admin)
    return render(request, 'Administrativo/administradores/agregar.html', {'form': form, 'admin': admin, })

def AdminEliminar(request, id):
    admin = get_object_or_404(models.administradores, id=id)
    admin.delete()
    messages.add_message(request, messages.INFO, 'El administrador : {0} ha sido borrado '.format(admin.username))
    return HttpResponseRedirect(reverse('main:admin_consultar'))

def AdminConsultar(request):
    admin = models.administradores.objects.filter(is_staff=True).order_by('username') 
    return render(request, 'Administrativo/administradores/consultar.html', {'admin' : admin})

# --  ALUMNOS -- 

def AlumnoAlta(request):
    if request.method == 'POST':
        form = forms.Alumnoform(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_staff = False
            instance.is_superuser = False
            instance.save()
            messages.add_message(request, messages.INFO, 'El alumno ha sido agregado exitosamente ')
            return HttpResponseRedirect(reverse('main:alumno_consultar'))
        else:
            return render(request, 'Administrativo/alumnos/agregar.html', {'form': form})
    else:
        form = forms.Alumnoform()
    return render(request, 'Administrativo/alumnos/agregar.html', {'form': form})

def AlumnoEditar(request, id):
    alumnos = get_object_or_404(models.administradores, id=id)
    if request.method == 'POST':
        form = forms.Alumnoform(request.POST, instance=alumnos)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'El alumno ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:alumno_consultar'))
        else:
            return render(request, 'Administrativo/alumnos/agregar.html', {'form': form, 'alumnos': alumnos, })
    else:
        form = forms.Alumnoform(instance=alumnos)
    return render(request, 'Administrativo/alumnos/agregar.html', {'form': form, 'alumnos': alumnos, })

def AlumnoEliminar(request, id):
    alumnos = get_object_or_404(models.administradores, id=id)
    alumnos.delete()
    messages.add_message(request, messages.INFO, 'El alumno : {0} ha sido borrado '.format(alumnos.username))
    return HttpResponseRedirect(reverse('main:alumno_consultar'))

def AlumnoConsultar(request):
    alumnos = models.administradores.objects.filter(is_staff=False).order_by('username') 
    return render(request, 'Administrativo/alumnos/consultar.html', {'alumnos' : alumnos})

# --  CARRERAS -- 

def CarreraAlta(request):
    if request.method == 'POST':
        form = forms.Carreraform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'La carrera ha sido agregada exitosamente ')
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
            messages.add_message(request, messages.INFO, 'La carrera ha sido modificada exitosamente ')
            return HttpResponseRedirect(reverse('main:carrera_consultar'))
        else:
            return render(request, 'Administrativo/carreras/agregar.html', {'form': form, 'carreras': carreras, })
    else:
        form = forms.Carreraform(instance=carreras)
    return render(request, 'Administrativo/carreras/agregar.html', {'form': form, 'carreras': carreras, })

def CarreraEliminar(request, id):
    carreras = get_object_or_404(models.Carrera, id=id)
    carreras.delete()
    messages.add_message(request, messages.INFO, 'La carrera : {0} ha sido borrada '.format(carreras.Nombre.encode('utf8')))
    return HttpResponseRedirect(reverse('main:carrera_consultar'))

def CarreraConsultar(request):
    carreras = models.Carrera.objects.all().order_by('Nombre')    
    return render(request, 'Administrativo/carreras/consultar.html', {'carreras' : carreras})


# --  MAESTROS -- 

def MaestroAlta(request):
    if request.method == 'POST':
        form = forms.Maestroform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'El maestro ha sido agregado exitosamente ')
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
            messages.add_message(request, messages.INFO, 'El maestro ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:maestro_consultar'))
        else:
            return render(request, 'Administrativo/maestros/agregar.html', {'form': form, 'maestros': maestros, })
    else:
        form = forms.Maestroform(instance=maestros)
    return render(request, 'Administrativo/maestros/agregar.html', {'form': form, 'maestros': maestros, })

def MaestroEliminar(request, id):
    maestros = get_object_or_404(models.Maestro, id=id)
    maestros.delete()
    messages.add_message(request, messages.INFO, 'El maestro : {0} ha sido borrado '.format(maestros.Nombre.encode('utf8')))
    return HttpResponseRedirect(reverse('main:maestro_consultar'))

def MaestroConsultar(request):
    maestros = models.Maestro.objects.all().order_by('Nombre') 
    return render(request, 'Administrativo/maestros/consultar.html', {'maestros' : maestros,})

# --  TUTORES -- 

def TutorAlta(request):
    if request.method == 'POST':
        form = forms.Tutorform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'El tutor ha sido agregado exitosamente ')
            return HttpResponseRedirect(reverse('main:tutor_consultar'))
        else:
            return render(request, 'Administrativo/tutores/agregar.html', {'form': form})
    else:
        form = forms.Tutorform()
    return render(request, 'Administrativo/tutores/agregar.html', {'form': form})

def TutorEditar(request, id):
    tutores = get_object_or_404(models.Tutor, id=id)
    if request.method == 'POST':
        form = forms.Tutorform(request.POST, instance=tutores)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'El tutor ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:tutor_consultar'))
        else:
            return render(request, 'Administrativo/tutores/agregar.html', {'form': form, 'tutores': tutores, })
    else:
        form = forms.Tutorform(instance=tutores)
    return render(request, 'Administrativo/tutores/agregar.html', {'form': form, 'tutores': tutores, })

def TutorEliminar(request, id):
    tutores = get_object_or_404(models.Tutor, id=id)
    tutores.delete()
    messages.add_message(request, messages.INFO, 'El tutor : {0} ha sido borrado '.format(tutores.Maestro))
    return HttpResponseRedirect(reverse('main:tutor_consultar'))

def TutorConsultar(request):
    tutores = models.Tutor.objects.all().order_by(Lower('Maestro').desc())    
    return render(request, 'Administrativo/tutores/consultar.html', {'tutores' : tutores})

# --  GRUPOS -- 

def GrupoAlta(request):
    if request.method == 'POST':
        form = forms.Grupoform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'El grupo ha sido agregado exitosamente ')
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
            messages.add_message(request, messages.INFO, 'El grupo ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:grupo_consultar'))
        else:
            return render(request, 'Administrativo/grupos/agregar.html', {'form': form, 'grupos': grupos, })
    else:
        form = forms.Grupoform(instance=grupos)
    return render(request, 'Administrativo/grupos/agregar.html', {'form': form, 'grupos': grupos, })

def GrupoEliminar(request, id):
    grupos = get_object_or_404(models.Grupo, id=id)
    grupos.delete()
    messages.add_message(request, messages.INFO, 'El grupo ha sido borrado '.format(grupos.Cuatrimestre))
    return HttpResponseRedirect(reverse('main:grupo_consultar'))

def GrupoConsultar(request):
    grupos = models.Grupo.objects.all().order_by('Cuatrimestre')    
    return render(request, 'Administrativo/grupos/consultar.html', {'grupos' : grupos})

# --  JEFES DE CARRERAS -- 

def JefeCarreraAlta(request):
    if request.method == 'POST':
        form = forms.JefeCarreraform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'El jefe de carrera ha sido agregado exitosamente ')
            return HttpResponseRedirect(reverse('main:jefe_carrera_consultar'))
        else:
            return render(request, 'Administrativo/jefes_carreras/agregar.html', {'form': form})
    else:
        form = forms.JefeCarreraform()
    return render(request, 'Administrativo/jefes_carreras/agregar.html', {'form': form})

def JefeCarreraEditar(request, id):
    jefescarreras = get_object_or_404(models.JefeCarrera, id=id)
    if request.method == 'POST':
        form = forms.JefeCarreraform(request.POST, instance=jefescarreras)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'El jefe de carrera ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:jefe_carrera_consultar'))
        else:
            return render(request, 'Administrativo/jefes_carreras/agregar.html', {'form': form, 'jefescarreras': jefescarreras, })
    else:
        form = forms.JefeCarreraform(instance=jefescarreras)
    return render(request, 'Administrativo/jefes_carreras/agregar.html', {'form': form, 'jefescarreras': jefescarreras, })

def JefeCarreraEliminar(request, id):
    jefescarreras = get_object_or_404(models.JefeCarrera, id=id)
    jefescarreras.delete()
    messages.add_message(request, messages.INFO, 'El jefe de carrera : {0} ha sido borrado '.format(jefescarreras.Nombre.encode('utf8')))
    return HttpResponseRedirect(reverse('main:jefe_carrera_consultar'))

def JefeCarreraConsultar(request):
    jefescarreras = models.JefeCarrera.objects.all().order_by('Nombre')    
    return render(request, 'Administrativo/jefes_carreras/consultar.html', {'jefescarreras' : jefescarreras})

# -- MATERIAS -- 

def MateriaAlta(request):
    if request.method == 'POST':
        form = forms.Materiaform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'La materia ha sido agregada exitosamente ')
            return HttpResponseRedirect(reverse('main:materia_consultar'))
        else:
            return render(request, 'Administrativo/materias/agregar.html', {'form': form})
    else:
        form = forms.Materiaform()
    return render(request, 'Administrativo/materias/agregar.html', {'form': form})

def MateriaEditar(request, id):
    materias = get_object_or_404(models.Materia, id=id)
    if request.method == 'POST':
        form = forms.Materiaform(request.POST, instance=materias)
        if form.is_valid():
            form = form.save()
            messages.add_message(request, messages.INFO, 'La materia ha sido modificada exitosamente ')
            return HttpResponseRedirect(reverse('main:materia_consultar'))
        else:
            return render(request, 'Administrativo/materias/agregar.html', {'form': form, 'materias': materias, })
    else:
        form = forms.Materiaform(instance=materias)
    return render(request, 'Administrativo/materias/agregar.html', {'form': form, 'materias': materias, })

def MateriaEliminar(request, id):
    materias = get_object_or_404(models.Materia, id=id)
    materias.delete()
    messages.add_message(request, messages.INFO, 'La materia : {0} ha sido borrada '.format(materias.Nombre.encode('utf8')))
    return HttpResponseRedirect(reverse('main:materia_consultar'))

def MateriaConsultar(request):
    materias = models.Materia.objects.all().order_by('Nombre')    
    return render(request, 'Administrativo/materias/consultar.html', {'materias' : materias})


    # --  CATALOGO -- 

def CatalogoAlta(request):
    if request.method == 'POST':
        form = forms.Catalagoform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'El catalago ha sido agregado exitosamente ')
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
            messages.add_message(request, messages.INFO, 'El catalago ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:catalogo_consultar'))
        else:
            return render(request, 'Administrativo/Catalogo/agregar.html', {'form': form, 'catalago': catalago, })
    else:
        form = forms.Catalagoform(instance=catalago)
    return render(request, 'Administrativo/Catalogo/agregar.html', {'form': form, 'catalago': catalago, })

def CatalogoEliminar(request, id):
    catalago = get_object_or_404(models.Catalago, id=id)
    catalago.delete()
    messages.add_message(request, messages.INFO, 'El Catalago : {0} ha sido borrado '.format(catalago.Descripcion.encode('utf8')))
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
            messages.add_message(request, messages.INFO, 'El periodo ha sido agregado exitosamente ')
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
            messages.add_message(request, messages.INFO, 'El periodo ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:periodo_consultar'))
        else:
            return render(request, 'Administrativo/Periodo/agregar.html', {'form': form, 'catalago': catalago, })
    else:
        form = forms.Periodoform(instance=periodo)
    return render(request, 'Administrativo/Periodo/agregar.html', {'form': form, 'periodo': periodo, })

def PeriodoEliminar(request, id):
    periodo = get_object_or_404(models.Periodo, id=id)
    periodo.delete()
    messages.add_message(request, messages.INFO, 'El periodo : {0} ha sido borrado '.format(periodo.Descripcion.encode('utf8')))
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
            messages.add_message(request, messages.INFO, 'La sección ha sido agregado exitosamente ')
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
            messages.add_message(request, messages.INFO, 'La sección ha sido modificada exitosamente ')
            return HttpResponseRedirect(reverse('main:seccion_consultar'))
        else:
            return render(request, 'Administrativo/Seccion/agregar.html', {'form': form, 'seccion': seccion, })
    else:
        form = forms.Seccionform(instance=seccion)
    return render(request, 'Administrativo/Periodo/agregar.html', {'form': form, 'seccion': seccion, })

def SeccionEliminar(request, id):
    seccion = get_object_or_404(models.Seccion, id=id)
    seccion.delete()
    messages.add_message(request, messages.INFO, 'Seccion : {0} ha sido borrada '.format(seccion.Descripcion.encode('utf8')))
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
            messages.add_message(request, messages.INFO, 'La pregunta ha sido agregado exitosamente ')
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
            messages.add_message(request, messages.INFO, 'La pregunta ha sido modificada exitosamente ')
            return HttpResponseRedirect(reverse('main:pregunta_consultar'))
        else:
            return render(request, 'Administrativo/Pregunta/agregar.html', {'form': form, 'pregunta': pregunta, })
    else:
        form = forms.Preguntaform(instance=pregunta)
    return render(request, 'Administrativo/Pregunta/agregar.html', {'form': form, 'pregunta': pregunta, })

def PreguntaEliminar(request, id):
    pregunta = get_object_or_404(models.Pregunta, id=id)
    pregunta.delete()
    messages.add_message(request, messages.INFO, 'La pregunta : {0} ha sido borrada '.format(pregunta.Descripcion.encode('utf8')))
    return HttpResponseRedirect(reverse('main:pregunta_consultar'))

def PreguntaConsultar(request):
    pregunta = models.Pregunta.objects.all()   
    return render(request, 'Administrativo/Pregunta/consultar.html', {'pregunta' : pregunta})

#  --Evaluacion--
def CatalogoPreguntas(request):
    periodo = models.Periodo.objects.filter(Realizado=False)
    cat = periodo[0].Catalagos.all()[0]
    seccion = cat.Secciones.all()[0]
    pregunta = seccion.Preguntas.all()
    materias =  models.Materia.objects.filter(Carrera=1).filter(Grupos=1)#las filtra por grupo tambien
  #  materias =  models.Materia.objects.filter(Carrera=1)
    maestros = models.Maestro.objects.filter(Materia__in=materias)
    
    return render(request, 'sieda/Evaluacion/consultar.html', {'seccion' : seccion, 'preguntas' : pregunta, 'materias' : materias, 'maestros':maestros, 'NumSeccion' : 0})

def Maestros_lista(request):
    data = serializers.serialize("json",models.Maestro.objects.all())
    return HttpResponse(data,content_type='application/json')

def Secciones_lista(request):
    data = serializers.serialize("json",models.Seccion.objects.all())
    return HttpResponse(data,content_type='application/json')

def Jefes_lista(request):
    data = serializers.serialize("json",models.JefeCarrera.objects.all())
    return HttpResponse(data,content_type='application/json')

def Preguntas_lista(request):
    data = serializers.serialize("json",models.Pregunta.objects.all())
    return HttpResponse(data,content_type='application/json')

def GuardarEvaluacion(request,id):
    periodo = models.Periodo.objects.filter(Realizado=False)
    cat = periodo[0].Catalagos.all()[0]
    sec = int(id)
    seccion = cat.Secciones.all()[sec]
    pregunta = seccion.Preguntas.all()
    maestros = models.Maestro.objects.all() 
    materias =  models.Materia.objects.filter(Carrera=1)
    secciones_totales = cat.Secciones.count()
    cal = 0

    for mat in materias:
            for pre in pregunta:
                cal = cal + int(request.POST.get(str(pre.id)+""+str(mat.id),False))

            cali = models.Calificaciones(Periodo=periodo[0], Seccion=seccion, Calificacion=cal)
            cali.save()
            cal = 0
    
    
    var = secciones_totales -1

    if var == sec:
        return render(request, 'sieda/Evaluacion/fin.html')
    else:
        secNuevo = sec + 1
        seccionNueva = cat.Secciones.all()[secNuevo]
        preguntaNueva = seccionNueva.Preguntas.all()
        template = loader.get_template('sieda/Evaluacion/consultar.html')
        context = {'seccion' : seccionNueva, 'preguntas' : preguntaNueva, 'materias' : materias,'maestros':maestros, 'NumSeccion' : secNuevo}
        return HttpResponse(template.render(context, request))


