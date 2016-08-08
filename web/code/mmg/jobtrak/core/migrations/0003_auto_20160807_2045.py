# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-08 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_joblisting_job_functions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joblisting',
            name='job_functions',
        ),
        migrations.AddField(
            model_name='joblisting',
            name='area_of_focus',
            field=models.CharField(blank=True, default=b'', max_length=128),
        ),
        migrations.AddField(
            model_name='joblisting',
            name='employment_type',
            field=models.CharField(blank=True, default=b'', max_length=64),
        ),
        migrations.AddField(
            model_name='joblisting',
            name='job_fuction',
            field=models.CharField(blank=True, default=b'', max_length=128),
        ),
    ]