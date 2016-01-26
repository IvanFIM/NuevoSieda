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

    url(r'^Encuesta', views.Encuesta, name='sieda_encuesta'),
    url(r'^Sieda-admin$', views.AdminMain, name='admin_main'),
    url(r'^administradores/alta$', views.AdminAlta, name='admin_alta'),
    url(r'^administradores/consultar$', views.AdminConsultar, name='admin_consultar'),
    url(r'^administradores/(?P<id>[0-9]+)/eliminar$', views.AdminEliminar, name='admin_eliminar'),
    url(r'^administradores/(?P<id>[0-9]+)/modificar$', views.AdminEditar, name='admin_editar'),
    
]
