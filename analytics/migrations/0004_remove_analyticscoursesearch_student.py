# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-05 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_analyticscoursesearch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analyticscoursesearch',
            name='student',
        ),
    ]
