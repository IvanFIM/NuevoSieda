# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-09 22:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20160408_0914'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalago',
            options={'ordering': ['Descripcion']},
        ),
        migrations.AlterModelOptions(
            name='pregunta',
            options={'ordering': ['Descripcion']},
        ),
        migrations.AlterModelOptions(
            name='seccion',
            options={'ordering': ['Descripcion']},
        ),
    ]