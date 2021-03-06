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
from .models import administradores, Carrera, Maestro, Grupo, Tutor, JefeCarrera, Materia, Seccion, Comentarios, Periodo, Catalago
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required ,permission_required
from django.db.models import F, Count, Sum,Q
import json as simplejson
import json

# Handle 404 Errors
def error404(request):
    template = loader.get_template('error.htm')
    context = Context({
        'message': 'All: %s' % request,
        })
    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)

def Error(request):
    return render(request, 'error.html' )

def Cerrar(request):
    return render(request, 'cerrar.html' )

###### -- PORTAL SIEDA -- ######

def SiedaMain(request):
    return render(request, 'sieda/login.html' )

@login_required(login_url='/')
def Evaluacion(request):
    if not request.user.is_staff:
        per = models.Periodo.objects.filter(Realizado=False)
        return render(request, 'sieda/Evaluacion/index.html', {'per' :per })
    return HttpResponseRedirect(reverse('main:admin_main'))

@login_required(login_url='/')
def Evaluacion_sencilla(request,id):
    per = models.Periodo.objects.filter(Realizado=False)
    cat = per[0].Catalagos.get(id=id)
    seccion = cat.Secciones.all()[0]
    pregunta = seccion.Preguntas.all()


    return render(request, 'sieda/Evaluacion/Evaluacion_sencilla.html', {'seccion' :seccion ,'preguntas':pregunta, 'catalogo':cat, 'NumSeccion' : 0})

@login_required(login_url='/')
def Fin(request):
    per = models.Periodo.objects.filter(Realizado=False)
    cat = per[0].Catalagos.get(id=int(request.POST.get("cat",False)))
    comen = models.Comentarios(Periodo=per[0],Alumno = request.user,Catalogo = cat, Comentario= request.POST.get("comen",False))
    comen.save()
    cat.alumnos.add(request.user)
    cat.save()
    messages.add_message(request, messages.INFO, 'Se ha realizado la evaluación correctamente.')
    return HttpResponseRedirect(reverse('main:Evaluacion'))



###### -- PORTAL ADMINISTRATIVO -- ######
@login_required(login_url='/')
def AdminMain(request):
    if not request.user.is_staff:
        return HttpResponseRedirect(reverse('main:Evaluacion'))
    maestros_total = Maestro.objects.count()
    alumnos_total = administradores.objects.filter(is_staff=False).count()
    carreras_total = Carrera.objects.count()
    comentarios_total = models.Comentarios.objects.count()
    
    c = models.Catalago.objects.filter(EvaluacionSencilla=False).aggregate(num=Count('alumnos'))
    alumnos_faltantes = alumnos_total- c['num']

    return render(request, 'administrativo/index.html' , {'comentarios_total': comentarios_total, 
        'alumnos_total':alumnos_total, 'carreras_total':carreras_total, 'alumnos_faltantes':alumnos_faltantes,})

# -- ADMINISTRADORES -- 
@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def AdminEliminar(request, id):
    admin = get_object_or_404(models.administradores, id=id)
    admin.delete()
    messages.add_message(request, messages.INFO, 'El administrador : {0} ha sido borrado '.format(admin.username))
    return HttpResponseRedirect(reverse('main:admin_consultar'))

@login_required(login_url='/')
def AdminConsultar(request):
    admin = models.administradores.objects.filter(is_staff=True).order_by('username') 
    return render(request, 'Administrativo/administradores/consultar.html', {'admin' : admin})

# --  ALUMNOS -- 
@login_required(login_url='/')
def AlumnoAlta(request):
    if request.method == 'POST':
        if request.POST.get('btnGuardar'):
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
        elif request.POST.get('btnAgregarOtro'):
            form = forms.Alumnoform(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.is_staff = False
                instance.is_superuser = False
                instance.save()
                messages.add_message(request, messages.INFO, 'El alumno ha sido agregado exitosamente ')
            else:
                return render(request, 'Administrativo/alumnos/agregar.html', {'form': form})
    else:
        form = forms.Alumnoform()
    return render(request, 'Administrativo/alumnos/agregar.html', {'form': form})

@login_required(login_url='/')
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

@login_required(login_url='/')
def AlumnoEliminar(request, id):
    alumnos = get_object_or_404(models.administradores, id=id)
    alumnos.delete()
    messages.add_message(request, messages.INFO, 'El alumno : {0} ha sido borrado '.format(alumnos.username))
    return HttpResponseRedirect(reverse('main:alumno_consultar'))

@login_required(login_url='/')
def AlumnoConsultar(request):
    alumnos = models.administradores.objects.filter(is_staff=False).order_by('Carrera') 
    return render(request, 'Administrativo/alumnos/consultar.html', {'alumnos' : alumnos})

# --  CARRERAS -- 
@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def CarreraEliminar(request, id):
    carreras = get_object_or_404(models.Carrera, id=id)
    carreras.delete()
    messages.add_message(request, messages.INFO, 'La carrera : {0} ha sido borrada '.format(carreras.Nombre.encode('utf8')))
    return HttpResponseRedirect(reverse('main:carrera_consultar'))

@login_required(login_url='/')
def CarreraConsultar(request):
    carreras = models.Carrera.objects.all()  
    return render(request, 'Administrativo/carreras/consultar.html', {'carreras' : carreras})


# --  MAESTROS -- 
@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def MaestroEliminar(request, id):
    maestros = get_object_or_404(models.Maestro, id=id)
    maestros.delete()
    messages.add_message(request, messages.INFO, 'El maestro : {0} ha sido borrado '.format(maestros.Nombre.encode('utf8')))
    return HttpResponseRedirect(reverse('main:maestro_consultar'))

@login_required(login_url='/')
def MaestroConsultar(request):
    maestros = models.Maestro.objects.all()
    return render(request, 'Administrativo/maestros/consultar.html', {'maestros' : maestros,})

# --  TUTORES -- 
@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def TutorEliminar(request, id):
    tutores = get_object_or_404(models.Tutor, id=id)
    tutores.delete()
    messages.add_message(request, messages.INFO, 'El tutor : {0} ha sido borrado '.format(tutores.Maestro))
    return HttpResponseRedirect(reverse('main:tutor_consultar'))

@login_required(login_url='/')
def TutorConsultar(request):
    tutores = models.Tutor.objects.all()    
    return render(request, 'Administrativo/tutores/consultar.html', {'tutores' : tutores})

# --  GRUPOS -- 
@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def GrupoEliminar(request, id):
    grupos = get_object_or_404(models.Grupo, id=id)
    grupos.delete()
    messages.add_message(request, messages.INFO, 'El grupo ha sido borrado '.format(grupos.Cuatrimestre))
    return HttpResponseRedirect(reverse('main:grupo_consultar'))

@login_required(login_url='/')
def GrupoConsultar(request):
    grupos = models.Grupo.objects.all()  
    return render(request, 'Administrativo/grupos/consultar.html', {'grupos' : grupos})

# --  JEFES DE CARRERAS -- 
@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def JefeCarreraEliminar(request, id):
    jefescarreras = get_object_or_404(models.JefeCarrera, id=id)
    jefescarreras.delete()
    messages.add_message(request, messages.INFO, 'El jefe de carrera : {0} ha sido borrado '.format(jefescarreras.Nombre.encode('utf8')))
    return HttpResponseRedirect(reverse('main:jefe_carrera_consultar'))

@login_required(login_url='/')
def JefeCarreraConsultar(request):
    jefescarreras = models.JefeCarrera.objects.all()   
    return render(request, 'Administrativo/jefes_carreras/consultar.html', {'jefescarreras' : jefescarreras})

# -- MATERIAS -- 
@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def MateriaEliminar(request, id):
    materias = get_object_or_404(models.Materia, id=id)
    materias.delete()
    messages.add_message(request, messages.INFO, 'La materia : {0} ha sido borrada '.format(materias.Nombre.encode('utf8')))
    return HttpResponseRedirect(reverse('main:materia_consultar'))

@login_required(login_url='/')
def MateriaConsultar(request):
    materias = models.Materia.objects.all()    
    return render(request, 'Administrativo/materias/consultar.html', {'materias' : materias})


    # --  CATALOGO -- 
@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def CatalogoEliminar(request, id):
    catalago = get_object_or_404(models.Catalago, id=id)
    catalago.delete()
    messages.add_message(request, messages.INFO, 'El Catalago : {0} ha sido borrado '.format(catalago.Descripcion.encode('utf8')))
    return HttpResponseRedirect(reverse('main:catalogo_consultar'))

@login_required(login_url='/')
def CatalogoConsultar(request):
    catalago = models.Catalago.objects.all()   
    return render(request, 'Administrativo/Catalogo/consultar.html', {'catalago' : catalago})

    # --  PERIODO -- 
@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def PeriodoEliminar(request, id):
    periodo = get_object_or_404(models.Periodo, id=id)
    periodo.delete()
    messages.add_message(request, messages.INFO, 'El periodo : {0} ha sido borrado '.format(periodo.Descripcion.encode('utf8')))
    return HttpResponseRedirect(reverse('main:periodo_consultar'))

@login_required(login_url='/')
def PeriodoConsultar(request):
    periodo = models.Periodo.objects.all()   
    return render(request, 'Administrativo/Periodo/consultar.html', {'periodo' : periodo})

    # --  SECCION -- 
@login_required(login_url='/')
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
@login_required(login_url='/')
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
    return render(request, 'Administrativo/Seccion/agregar.html', {'form': form, 'seccion': seccion, })

@login_required(login_url='/')
def SeccionEliminar(request, id):
    seccion = get_object_or_404(models.Seccion, id=id)
    seccion.delete()
    messages.add_message(request, messages.INFO, 'Seccion : {0} ha sido borrada '.format(seccion.Descripcion.encode('utf8')))
    return HttpResponseRedirect(reverse('main:seccion_consultar'))

@login_required(login_url='/')
def SeccionConsultar(request):
    seccion = models.Seccion.objects.all()   
    return render(request, 'Administrativo/Seccion/consultar.html', {'seccion' : seccion})

    # --  PREGUNTA -- 
@login_required(login_url='/')
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

@login_required(login_url='/')
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

@login_required(login_url='/')
def PreguntaEliminar(request, id):
    pregunta = get_object_or_404(models.Pregunta, id=id)
    pregunta.delete()
    messages.add_message(request, messages.INFO, 'La pregunta : {0} ha sido borrada '.format(pregunta.Descripcion.encode('utf8')))
    return HttpResponseRedirect(reverse('main:pregunta_consultar'))

@login_required(login_url='/')
def PreguntaConsultar(request):
    pregunta = models.Pregunta.objects.all()   
    return render(request, 'Administrativo/Pregunta/consultar.html', {'pregunta' : pregunta})

#  --Evaluacion--
@login_required(login_url='/')
def CatalogoPreguntas(request,id):
    periodo = models.Periodo.objects.filter(Realizado=False)
    cat = periodo[0].Catalagos.get(id=id)
    seccion = cat.Secciones.all()[0]
    pregunta = seccion.Preguntas.all()
    materias =  models.Materia.objects.filter(Carrera=request.user.Carrera,Grupos= request.user.Grupo.id)#las filtra por grupo tambien
    Maes_list = []
    for file in materias:
        file_info = {}
        
        nomMaestro = models.Maestro.objects.filter(Grupos= request.user.Grupo.id,Materia=file.id)
        for n in nomMaestro:
            file_info['id'] = file.id
            file_info['maestro'] = n.Nombre
            file_info['materia'] = file.Nombre
            file_info['abrev'] = file.Abrev_materia
            Maes_list.append(file_info)

    return render(request, 'sieda/Evaluacion/consultar.html', {'seccion' : seccion, 'catalogo': cat, 'preguntas' : pregunta, 'maestros':Maes_list, 'NumSeccion' : 0})


@login_required(login_url='/')
def Maestros_lista(request):
    data = serializers.serialize("json",models.Maestro.objects.all())
    return HttpResponse(data,content_type='application/json')

@login_required(login_url='/')
def Secciones_lista(request):
    data = serializers.serialize("json",models.Seccion.objects.all())
    return HttpResponse(data,content_type='application/json')

@login_required(login_url='/')
def Jefes_lista(request):
    data = serializers.serialize("json",models.JefeCarrera.objects.all())
    return HttpResponse(data,content_type='application/json')

@login_required(login_url='/')
def Preguntas_lista(request):
    data = serializers.serialize("json",models.Pregunta.objects.all())
    return HttpResponse(data,content_type='application/json')

# --  REPORTES -- 
@login_required(login_url='/')
def Reporte_menu(request):
    maestros = models.Maestro.objects.values('id','Nombre').order_by('Nombre').distinct()
    tutores = models.Tutor.objects.values('Maestro','Maestro__Nombre').order_by('Maestro__Nombre').distinct()
    grupos = models.Grupo.objects.all().order_by('Cuatrimestre')    
    carreras = models.Carrera.objects.all().order_by('Nombre')   
    return render(request, 'Administrativo/reportes/reportes_menu.html',{'grupos' : grupos, 'carreras':carreras, 'tutores':tutores,'maestros':maestros} )

@login_required(login_url='/')
def Reporte_grupal(request): 
    return render(request, 'Administrativo/reportes/reporte_grupal.html')

@login_required(login_url='/')
def Lista_grupal(request):
    idgrupo = request.GET.get('grupo')
    idcarera= request.GET.get('carrera')


    periodo = models.Periodo.objects.filter(Realizado=False).get()
    cat = periodo.Catalagos.filter(EvaluacionSencilla =False).values('Secciones').count()
 
    data = json.dumps([dict(item) for item in models.Calificaciones.objects.filter(Materia__Grupos=idgrupo,Materia__Carrera=idcarera)\
        .filter(Grupo_id=idgrupo).exclude(Maestro_id=None).values('Maestro_id__Nombre')\
        .annotate(num=(Count('Maestro_id')/cat))\
        .annotate(puntos=Sum('Calificacion'))\
        .annotate(total=F('puntos') / F('num'))\
        .order_by('total')])
    return HttpResponse(data,content_type='application/json')

@login_required(login_url='/')
def Reporte_general_maestros(request):
   
    return render(request, 'Administrativo/reportes/reporte_general_maestros.html' )

@login_required(login_url='/')
def Lista_general_maestros(request):
    periodo = models.Periodo.objects.filter(Realizado=False).get()
    cat = periodo.Catalagos.filter(EvaluacionSencilla =False).values('Secciones').count()
 
    data = json.dumps([dict(item) for item in models.Calificaciones.objects.exclude(Maestro_id=None).values('Maestro_id__Nombre')\
        .annotate(num=(Count('Maestro_id')/cat))\
        .annotate(puntos=Sum('Calificacion'))\
        .annotate(total=F('puntos') / F('num'))\
        .order_by('total')])
    return HttpResponse(data,content_type='application/json')

@login_required(login_url='/')
def Reporte_esp_maestros(request):
    maestro = request.POST['maestro']
    materias = models.Maestro.objects.filter(id = maestro)

    periodo = models.Periodo.objects.filter(Realizado=False)

    tutor= models.Calificaciones.objects.all().filter(Tutor_id__Maestro_id = maestro)\
    .values('Tutor_id__Maestro__Nombre','Tutor__Carrera__Nombre','Tutor__Grupo__Grupo','Tutor__Grupo__Cuatrimestre','Seccion__Descripcion')\
        .annotate(num=Count('Tutor_id'))\
        .annotate(puntos=Sum('Calificacion'))\
        .annotate(total=F('puntos') / F('num'))\
        .order_by('total')

    carrera_c = models.Maestro.objects.filter(id = maestro).values('Materia__Carrera__Nombre').annotate(num = Count('Materia__Carrera__Nombre'))

    maestro_e = models.Calificaciones.objects.filter(Maestro_id = maestro).exclude(Maestro_id=None)\
        .values('Maestro_id__Nombre','Seccion_id__Descripcion','Grupo__Cuatrimestre','Grupo__Grupo','Materia__Nombre','Periodo__Descripcion')\
        .annotate(num=Count('Maestro_id'))\
        .annotate(puntos=Sum('Calificacion'))\
        .annotate(total=F('puntos') / F('num'))\
        .order_by('Seccion_id','Maestro_id',)

    periodo = models.Periodo.objects.filter(Realizado=False).get()
    cat = periodo.Catalagos.filter(EvaluacionSencilla =False).values('Secciones').count()
 
    maestro_g = models.Calificaciones.objects.filter(Maestro_id=maestro)\
        .values('Materia_id__Nombre','Maestro_id__Nombre','Grupo_id__Grupo','Grupo_id__Cuatrimestre','Materia_id__Carrera__Nombre')\
        .annotate(num=(Count('Maestro_id')/cat))\
        .annotate(puntos=Sum('Calificacion'))\
        .annotate(total=F('puntos') / F('num'))\
        .order_by('total','Grupo_id')

    return render(request, 'Administrativo/reportes/reporte_esp_maestros.html',{'materias':materias,'carrera_c':carrera_c,'periodo':periodo\
        ,'tutor':tutor,'maestro_e':maestro_e,'maestro_g':maestro_g})

#-- REPORTE tutores listo---
@login_required(login_url='/')
def Reporte_general_tutores(request):
    return render(request, 'Administrativo/reportes/Reporte_general_tutores.html')

@login_required(login_url='/')
def Lista_general_tutores(request):
    data = json.dumps([dict(item) for item in models.Calificaciones.objects.exclude(Tutor_id=None).values('Tutor_id__Maestro__Nombre')\
        .annotate(num=Count('Tutor_id'))\
        .annotate(puntos=Sum('Calificacion'))\
        .annotate(total=F('puntos') / F('num'))\
        .order_by('total')])
    return HttpResponse(data,content_type='application/json')


@login_required(login_url='/')    
def Reporte_alumnos(request):
    tutor = request.POST['tutor']

    #Guardar en valiables el grupo y la carrera del tutor para filtrar los alumnos
    idgrupo = models.Tutor.objects.filter(Maestro=tutor).values_list('Grupo__id',flat=True)
    idcarrera = models.Tutor.objects.filter(Maestro=tutor).values_list('Carrera__id',flat=True)

    #Guardar en valiable los catalogos que hay en el periodo actual, para despues filtrar los alumnos que hicieron todos los catalogos
    catalogos = models.Periodo.objects.filter(Realizado=False).values_list('Catalagos',flat=True)
    
    #Guardar en valiable los alumnos que evaluaron Alguno de los catalogos   
    alumnos= models.Catalago.objects.filter(alumnos__catalago__in=catalogos).values('alumnos')

    #alumnos que no han hecho la evaluacion (para la tabla)
    alu_no= models.administradores.objects.filter(is_staff=False, Carrera__in=idcarrera, Grupo__in=idgrupo)\
   .order_by('Carrera','first_name')

    #alumnos que no han hecho la evaluacion (Alumnos tutorados faltantes:)
    alu_no_num= models.administradores.objects.filter(is_staff=False, Carrera__in=idcarrera, Grupo__in=idgrupo)\
    .exclude(id__in=alumnos).count()

    #alumnos que hicieron la evaluacion (Alumnos tutorados evaluados:)
    alu_si= models.administradores.objects.filter(is_staff=False, Carrera__in=idcarrera, Grupo__in=idgrupo)\
    .filter(id__in=alumnos).count()

    si_c= models.administradores.objects.filter(is_staff=False, Carrera__in=idcarrera, Grupo__in=idgrupo).filter(id__in=alumnos).values_list('id',flat=True)
    
    catalogos_al = models.Catalago.objects.filter(alumnos__in = si_c).values('alumnos__first_name','Descripcion').order_by('alumnos__first_name')

    return render(request, 'Administrativo/reportes/Reporte_alumnos.html', {'alu_no' : alu_no,'alu_si':alu_si,\
        'alu_no_num':alu_no_num,'alumnos':alumnos, 'catalogos_al':catalogos_al })
    
@login_required(login_url='/')
def GuardarEvaluacionSencilla(request,id):
    periodo = models.Periodo.objects.filter(Realizado=False)

    cat = periodo[0].Catalagos.get(id = int(request.POST.get("cat",False)))
    sec = int(id)
    seccion = cat.Secciones.all()[sec]
    pregunta = seccion.Preguntas.all()
    secciones_totales = cat.Secciones.count()
    cal = 0

    for pre in pregunta:
        cal = cal + int(request.POST.get(str(pre.id),False))

    tutor = models.Tutor.objects.filter(Grupo = request.user.Grupo)
    cali = models.Calificaciones(Periodo=periodo[0],Tutor = tutor[0], Catalogo= cat, Seccion=seccion, Calificacion=cal)
    cali.save()
    
    
    var = secciones_totales -1

    if var == sec:
        template = loader.get_template('sieda/Evaluacion/fin.html')
        context = {'catalogo': cat}
        return HttpResponse(template.render(context, request))
    else:
        secNuevo = sec + 1
        seccionNueva = cat.Secciones.all()[secNuevo]
        preguntaNueva = seccionNueva.Preguntas.all()
        template = loader.get_template('sieda/Evaluacion/Evaluacion_sencilla.html')
        context = {'seccion' : seccionNueva, 'preguntas' : preguntaNueva,'catalogo':cat,'NumSeccion' : secNuevo}
        return HttpResponse(template.render(context, request))

@login_required(login_url='/')
def GuardarEvaluacion(request,id):
    periodo = models.Periodo.objects.filter(Realizado=False)
    cat = periodo[0].Catalagos.get(id = int(request.POST.get("cat",False)))
    sec = int(id)
    seccion = cat.Secciones.all()[sec]
    pregunta = seccion.Preguntas.all()
    materias =  models.Materia.objects.filter(Carrera=request.user.Carrera,Grupos= request.user.Grupo.id)
    #materias =  models.Materia.objects.filter(Carrera=1).filter(Grupos=1)
    Maes_list = []
    for file in materias:
        file_info = {}
        nomMaestro = models.Maestro.objects.filter(Grupos= request.user.Grupo.id,Materia=file.id)
        for n in nomMaestro:
            file_info['id'] = file.id
            file_info['maestro'] = n.Nombre
            file_info['materia'] = file.Nombre
            file_info['abrev'] = file.Abrev_materia
            Maes_list.append(file_info)

    secciones_totales = cat.Secciones.count()
    cal = 0

    for mat in Maes_list:
        for pre in pregunta:
            cal = cal + int(request.POST.get(str(pre.id)+""+str(mat['id']),False))

        NMaestro = models.Maestro.objects.filter(Materia__id=int(mat['id'])).filter(Grupos= request.user.Grupo.id)
        Materia = models.Materia.objects.get(id = mat['id'])
        cali = models.Calificaciones(Periodo=periodo[0], Maestro = NMaestro[0],Materia = Materia, Catalogo= cat, Seccion=seccion, Calificacion=cal, Grupo = request.user.Grupo)
        cali.save()
        cal = 0
    
    var = secciones_totales -1

    if var == sec:
        template = loader.get_template('sieda/Evaluacion/fin.html')
        context = {'catalogo': cat}
        return HttpResponse(template.render(context, request))
    else:
        secNuevo = sec + 1
        seccionNueva = cat.Secciones.all()[secNuevo]
        preguntaNueva = seccionNueva.Preguntas.all()
        template = loader.get_template('sieda/Evaluacion/consultar.html')
        context = {'seccion' : seccionNueva, 'preguntas' : preguntaNueva,'catalogo': cat,'maestros':Maes_list, 'NumSeccion' : secNuevo}
        return HttpResponse(template.render(context, request))



@login_required(login_url='/')
def ComentarioEliminar(request):

    comentario = request.POST.getlist('comentarios')

    for co in comentario:
        try:
            co=Comentarios.objects.get(pk=co)
            co.delete()
        except Comentarios.DoesNotExist:
            co = 0
    messages.add_message(request, messages.INFO, 'los comentarios ha sido borrados ')
    return HttpResponseRedirect(reverse('main:comentario_consultar'))


@login_required(login_url='/')
def ComentarioConsultar(request):
    comentario = Comentarios.objects.all()   
    return render(request, 'Administrativo/comentarios/consultar.html', {'comentario' : comentario})