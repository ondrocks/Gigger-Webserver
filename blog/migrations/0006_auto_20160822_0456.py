# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 04:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160815_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'managed': False, 'ordering': ['-created']},
        ),
    ]
