# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_jobboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobboard',
            name='last_click',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]