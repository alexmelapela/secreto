# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 12:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0006_auto_20160607_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='release',
        ),
    ]
