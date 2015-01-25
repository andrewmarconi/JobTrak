# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('jobtrak_core', '0006_auto_20150124_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('base_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Social Media Site',
                'verbose_name_plural': 'Social Media Sites',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.ForeignKey(blank=True, to='jobtrak_core.CompanyLocation', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='email_address',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='mobile_tel',
            field=models.CharField(blank=True, max_length=15, verbose_name=b'Mobile Phone', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='note',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='office_fax',
            field=models.CharField(blank=True, max_length=15, verbose_name=b'Office Fax', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='office_tel',
            field=models.CharField(blank=True, max_length=15, verbose_name=b'Office Phone', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
            preserve_default=True,
        ),
    ]
