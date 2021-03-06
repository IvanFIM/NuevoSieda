# -*- coding: utf-8 -*-
"""
URLS
"""
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from . import views
from django.conf.urls import handler404

urlpatterns = [
    #url(r'^$', views.SiedaMain, name='sieda_main'),
   

    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'sieda/login.html'}, name='login'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout',{'template_name':'cerrar.html'}, name='logout'),
    url(handler404,views.error404),

    #INDEX ADMINISTRADORES#
    url(r'^Sieda-admin$', views.AdminMain, name='admin_main'),
    #NUEVOS 
    url(r'^lista/maestros/$',views.Maestros_lista, name='LMaestro'),
    url(r'^lista/secciones/$',views.Secciones_lista, name='LSecciones'),
    url(r'^lista/jefes/$',views.Jefes_lista, name='LJefes'),
    url(r'^lista/preguntas/$',views.Preguntas_lista, name='LPregutas'),

    #REPORTES
    url(r'^Reporte/reporte_menu$',views.Reporte_menu, name='RMenu'),

    url(r'^Reporte/e_maestros$',views.Reporte_esp_maestros, name='REMaestros'),
   
    url(r'^Reporte/g_maestros$',views.Reporte_general_maestros, name='RGMaestros'),
    url(r'^lista/g_maestros/$',views.Lista_general_maestros, name='LGMaestros'),
    url(r'^Reporte/g_tutores$',views.Reporte_general_tutores, name='RGTutores'),
    url(r'^lista/g_tutores/$',views.Lista_general_tutores, name='LGTutores'),
    
    url(r'^Reporte/grupos/$',views.Reporte_grupal, name='RGrupal'),
    url(r'^lista/grupos/$',views.Lista_grupal, name='LGrupal'),

    url(r'^Reporte/alumnos$',views.Reporte_alumnos, name='RAlumno'),

    #ABC'S#
    url(r'^administradores/alta$', views.AdminAlta, name='admin_alta'),
    url(r'^administradores/consultar$', views.AdminConsultar, name='admin_consultar'),
    url(r'^administradores/(?P<id>[0-9]+)/eliminar$', views.AdminEliminar, name='admin_eliminar'),
    url(r'^administradores/(?P<id>[0-9]+)/modificar$', views.AdminEditar, name='admin_editar'),

    url(r'^alumnos/alta$', views.AlumnoAlta, name='alumno_alta'),
    url(r'^alumnos/consultar$', views.AlumnoConsultar, name='alumno_consultar'),
    url(r'^alumnos/(?P<id>[0-9]+)/eliminar$', views.AlumnoEliminar, name='alumno_eliminar'),
    url(r'^alumnos/(?P<id>[0-9]+)/modificar$', views.AlumnoEditar, name='alumno_editar'),

    url(r'^carreras/alta$', views.CarreraAlta, name='carrera_alta'),
    url(r'^carreras/consultar$', views.CarreraConsultar, name='carrera_consultar'),
    url(r'^carreras/(?P<id>[0-9]+)/eliminar$', views.CarreraEliminar, name='carrera_eliminar'),
    url(r'^carreras/(?P<id>[0-9]+)/modificar$', views.CarreraEditar, name='carrera_editar'),

    url(r'^maestros/alta$', views.MaestroAlta, name='maestro_alta'),
    url(r'^maestros/consultar$', views.MaestroConsultar, name='maestro_consultar'),
    url(r'^maestros/(?P<id>[0-9]+)/eliminar$', views.MaestroEliminar, name='maestro_eliminar'),
    url(r'^maestros/(?P<id>[0-9]+)/modificar$', views.MaestroEditar, name='maestro_editar'),

    url(r'^tutores/alta$', views.TutorAlta, name='tutor_alta'),
    url(r'^tutores/consultar$', views.TutorConsultar, name='tutor_consultar'),
    url(r'^tutores/(?P<id>[0-9]+)/eliminar$', views.TutorEliminar, name='tutor_eliminar'),
    url(r'^tutores/(?P<id>[0-9]+)/modificar$', views.TutorEditar, name='tutor_editar'),
    
    url(r'^grupos/alta$', views.GrupoAlta, name='grupo_alta'),
    url(r'^grupos/consultar$', views.GrupoConsultar, name='grupo_consultar'),
    url(r'^grupos/(?P<id>[0-9]+)/eliminar$', views.GrupoEliminar, name='grupo_eliminar'),
    url(r'^grupos/(?P<id>[0-9]+)/modificar$', views.GrupoEditar, name='grupo_editar'),

    url(r'^materias/alta$', views.MateriaAlta, name='materia_alta'),
    url(r'^materias/consultar$', views.MateriaConsultar, name='materia_consultar'),
    url(r'^materias/(?P<id>[0-9]+)/eliminar$', views.MateriaEliminar, name='materia_eliminar'),
    url(r'^materias/(?P<id>[0-9]+)/modificar$', views.MateriaEditar, name='materia_editar'),
    
    url(r'^jefes_de_carreras/alta$', views.JefeCarreraAlta, name='jefe_carrera_alta'),
    url(r'^jefes_de_carreras/consultar$', views.JefeCarreraConsultar, name='jefe_carrera_consultar'),
    url(r'^jefes_de_carreras/(?P<id>[0-9]+)/eliminar$', views.JefeCarreraEliminar, name='jefe_carrera_eliminar'),
    url(r'^jefes_de_carreras/(?P<id>[0-9]+)/modificar$', views.JefeCarreraEditar, name='jefe_carrera_editar'),

    url(r'^Catalogo/alta$', views.CatalogoAlta, name='catalogo_alta'),
    url(r'^Catalogo/consultar$', views.CatalogoConsultar, name='catalogo_consultar'),
    url(r'^Catalogo/(?P<id>[0-9]+)/eliminar$', views.CatalogoEliminar, name='catalogo_eliminar'),
    url(r'^Catalogo/(?P<id>[0-9]+)/modificar$', views.CatalogoEditar, name='catalogo_editar'),

    url(r'^Periodo/alta$', views.PeriodoAlta, name='periodo_alta'),
    url(r'^Periodo/consultar$', views.PeriodoConsultar, name='periodo_consultar'),
    url(r'^Periodo/(?P<id>[0-9]+)/eliminar$', views.PeriodoEliminar, name='periodo_eliminar'),
    url(r'^Periodo/(?P<id>[0-9]+)/modificar$', views.PeriodoEditar, name='periodo_editar'),

    url(r'^Seccion/alta$', views.SeccionAlta, name='seccion_alta'),
    url(r'^Seccion/consultar$', views.SeccionConsultar, name='seccion_consultar'),
    url(r'^Seccion/(?P<id>[0-9]+)/eliminar$', views.SeccionEliminar, name='seccion_eliminar'),
    url(r'^Seccion/(?P<id>[0-9]+)/modificar$', views.SeccionEditar, name='seccion_editar'),

    url(r'^Pregunta/alta$', views.PreguntaAlta, name='pregunta_alta'),
    url(r'^Pregunta/consultar$', views.PreguntaConsultar, name='pregunta_consultar'),
    url(r'^Pregunta/(?P<id>[0-9]+)/eliminar$', views.PreguntaEliminar, name='pregunta_eliminar'),
    url(r'^Pregunta/(?P<id>[0-9]+)/modificar$', views.PreguntaEditar, name='pregunta_editar'),

    url(r'^Evaluacion/$', views.Evaluacion, name='Evaluacion'),
    url(r'^Evaluacion/Sencilla/(?P<id>[0-9]+)$', views.Evaluacion_sencilla, name='Evaluacion_sencilla'),
    url(r'^Evaluacion/consultar(?P<id>[0-9]+)$', views.CatalogoPreguntas, name='Evaluacion_consultar'),
    url(r'^Evaluacion/Guardar_evaluacionSencilla/(?P<id>[0-9]+)$', views.GuardarEvaluacionSencilla, name='Guardar_evaluacionSencilla'),
    url(r'^Evaluacion/Guardar_evaluacion/(?P<id>[0-9]+)$', views.GuardarEvaluacion, name='Guardar_evaluacion'),
    url(r'^Evaluacion/fin$', views.Fin, name='fin'),

    url(r'^Comentarios/consultar$', views.ComentarioConsultar, name='comentario_consultar'),
    url(r'^Comentarios/eliminar$', views.ComentarioEliminar, name='comentario_eliminar'),

    
]
 