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
    
]
