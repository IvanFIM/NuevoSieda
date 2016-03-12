# -*- encoding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.db.models.functions import Lower
from . import models
from . import forms
from .models import administradores, Alumno, Carrera, Maestro, Grupo, Tutor, JefeCarrera, Materia, Seccion


def Error(request):
    return render(request, 'error.html' )

###### -- PORTAL SIEDA -- ######

def SiedaMain(request):
    return render(request, 'sieda/index.html' )

def Encuesta(request):
    return render(request, 'sieda/Encuesta/encuesta.html' )

###### -- PORTAL ADMINISTRATIVO -- ######

def AdminMain(request):
    maestros_total = Maestro.objects.count()
    alumnos_total = Alumno.objects.count()
    carreras_total = Carrera.objects.count()
    tutores_total = Tutor.objects.count()
    alumnos_faltantes = Alumno.objects.filter(Realizado=False).count()


    return render(request, 'administrativo/index.html' , {'maestros_total': maestros_total, 
        'alumnos_total':alumnos_total, 'carreras_total':carreras_total, 'alumnos_faltantes':alumnos_faltantes,})

# -- ADMINISTRADORES -- 
def AdminAlta(request):
    if request.method == 'POST':
        form = forms.JefeCarreraform(request.POST or None)
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
    alumnos = models.Alumno.objects.all().order_by('Nombre')  
    return render(request, 'Administrativo/alumnos/consultar.html', {'alumnos' : alumnos})

# --  CARRERAS -- 

def CarreraAlta(request):
    if request.method == 'POST':
        form = forms.Carreraform(request.POST or None)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.INFO, 'Carrera ha sido agregado exitosamente ')
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
    messages.add_message(request, messages.INFO, 'Carrera : {0} ha sido borrada '.format(carreras.Nombre.encode('utf8')))
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
            messages.add_message(request, messages.INFO, 'Maestro ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:maestro_consultar'))
        else:
            return render(request, 'Administrativo/maestros/agregar.html', {'form': form, 'maestros': maestros, })
    else:
        form = forms.Maestroform(instance=maestros)
    return render(request, 'Administrativo/maestros/agregar.html', {'form': form, 'maestros': maestros, })

def MaestroEliminar(request, id):
    maestros = get_object_or_404(models.Maestro, id=id)
    maestros.delete()
    messages.add_message(request, messages.INFO, 'Maestro : {0} ha sido borrado '.format(maestros.Nombre.encode('utf8')))
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
            messages.add_message(request, messages.INFO, 'Tutor ha sido agregado exitosamente ')
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
            messages.add_message(request, messages.INFO, 'Tutor ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:tutor_consultar'))
        else:
            return render(request, 'Administrativo/tutores/agregar.html', {'form': form, 'tutores': tutores, })
    else:
        form = forms.Tutorform(instance=tutores)
    return render(request, 'Administrativo/tutores/agregar.html', {'form': form, 'tutores': tutores, })

def TutorEliminar(request, id):
    tutores = get_object_or_404(models.Tutor, id=id)
    tutores.delete()
    messages.add_message(request, messages.INFO, 'Tutor : {0} ha sido borrado '.format(tutores.Maestro))
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
            messages.add_message(request, messages.INFO, 'Grupo ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:grupo_consultar'))
        else:
            return render(request, 'Administrativo/grupos/agregar.html', {'form': form, 'grupos': grupos, })
    else:
        form = forms.Grupoform(instance=grupos)
    return render(request, 'Administrativo/grupos/agregar.html', {'form': form, 'grupos': grupos, })

def GrupoEliminar(request, id):
    grupos = get_object_or_404(models.Grupo, id=id)
    grupos.delete()
    messages.add_message(request, messages.INFO, 'Grupo ha sido borrado '.format(grupos.Cuatrimestre))
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
            messages.add_message(request, messages.INFO, 'Jefe de carrera ha sido agregado exitosamente ')
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
            messages.add_message(request, messages.INFO, 'Jefe de carrera ha sido modificado exitosamente ')
            return HttpResponseRedirect(reverse('main:jefe_carrera_consultar'))
        else:
            return render(request, 'Administrativo/jefes_carreras/agregar.html', {'form': form, 'jefescarreras': jefescarreras, })
    else:
        form = forms.JefeCarreraform(instance=jefescarreras)
    return render(request, 'Administrativo/jefes_carreras/agregar.html', {'form': form, 'jefescarreras': jefescarreras, })

def JefeCarreraEliminar(request, id):
    jefescarreras = get_object_or_404(models.JefeCarrera, id=id)
    jefescarreras.delete()
    messages.add_message(request, messages.INFO, 'Jefe de carrera : {0} ha sido borrado '.format(jefescarreras.Nombre.encode('utf8')))
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
            messages.add_message(request, messages.INFO, 'Materia ha sido agregado exitosamente ')
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
            messages.add_message(request, messages.INFO, 'Materia ha sido modificada exitosamente ')
            return HttpResponseRedirect(reverse('main:materia_consultar'))
        else:
            return render(request, 'Administrativo/materias/agregar.html', {'form': form, 'materias': materias, })
    else:
        form = forms.Materiaform(instance=materias)
    return render(request, 'Administrativo/materias/agregar.html', {'form': form, 'materias': materias, })

def MateriaEliminar(request, id):
    materias = get_object_or_404(models.Materia, id=id)
    materias.delete()
    messages.add_message(request, messages.INFO, 'Materia : {0} ha sido borrada '.format(materias.Nombre.encode('utf8')))
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
    messages.add_message(request, messages.INFO, 'Catalago : {0} ha sido borrada '.format(catalago.Descripcion.encode('utf8')))
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
    messages.add_message(request, messages.INFO, 'Periodo : {0} ha sido borrada '.format(periodo.Descripcion.encode('utf8')))
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
    messages.add_message(request, messages.INFO, 'Pregunta : {0} ha sido borrada '.format(pregunta.Descripcion.encode('utf8')))
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
    materias =  models.Materia.objects.filter(Carrera=7)
    maestros = models.Maestro.objects.all() 

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

def GuardarEvaluacion(request):
    periodo = models.Periodo.objects.filter(Realizado=False)
    cat = periodo[0].Catalagos.all()[0]
    sec = int(request.POST.get('NumSeccion',False))
    seccion = cat.Secciones.all()[sec]
    pregunta = seccion.Preguntas.all()
    materias =  models.Materia.objects.filter(Carrera=7)
    cal = 0
    
    for mat in materias:
        for pre in pregunta:
            cal = cal + int(request.POST.get(str(pre.id)+""+str(mat.id),False))

        cali = models.Calificaciones(Periodo=periodo[0], Seccion=seccion, Calificacion=cal)
        cali.save()
        cal = 0

    secNuevo = sec + 1
    seccionNueva = cat.Secciones.all()[secNuevo]
    preguntaNueva = seccionNueva.Preguntas.all()

    return render(request, 'sieda/Evaluacion/consultar.html', {'seccion' : seccionNueva, 'preguntas' : preguntaNueva, 'materias' : materias, 'NumSeccion' : secNuevo})
