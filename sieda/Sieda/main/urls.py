# -*- coding: utf-8 -*-
"""
URLS
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.SiedaMain, name='sieda_main'),

    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'sieda/index.html'}, name='login'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout', name='logout'),

    #INDEX ALUMNOS#
    url(r'^Encuesta', views.Encuesta, name='sieda_encuesta'),

    #INDEX ADMINISTRADORES#
    url(r'^Sieda-admin$', views.AdminMain, name='admin_main'),

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


    url(r'^Evaluacion/consultar$', views.CatalogoPreguntas, name='Evaluacion_consultar'),
    
]
