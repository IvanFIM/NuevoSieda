# -*- encoding: utf-8 -*-
"""Sieda URL Configuration
"""
from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   	url(r'^', include('main.urls', namespace='main')),
	
]
