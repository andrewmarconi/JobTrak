# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_line1', models.CharField(max_length=45, verbose_name='Address Line 1')),
                ('address_line2', models.CharField(max_length=45, verbose_name='Address line 2', blank=True)),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state_province', models.CharField(max_length=40, verbose_name='State/Province', blank=True)),
                ('postal_code', models.CharField(max_length=10, verbose_name='Postal Code', blank=True)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('note', models.TextField(null=True, verbose_name='Note', blank=True)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompanyLocation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('office_tel', models.CharField(blank=True, max_length=15, verbose_name='Office Phone', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('office_fax', models.CharField(blank=True, max_length=15, verbose_name='Office Fax', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('note', models.TextField(null=True, verbose_name='Note', blank=True)),
                ('address', models.ForeignKey(blank=True, to='contact.Address', null=True)),
                ('company', models.ForeignKey(to='contact.Company', null=True)),
            ],
            options={
                'verbose_name': 'Company Location',
                'verbose_name_plural': 'Company Locations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Company Type',
                'verbose_name_plural': 'Company Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=128, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=128, verbose_name='Last Name')),
                ('title', models.CharField(max_length=128, null=True, verbose_name='Title', blank=True)),
                ('email_address', models.EmailField(max_length=75, verbose_name='E-Mail Address', blank=True)),
                ('office_tel', models.CharField(blank=True, max_length=15, verbose_name='Office Phone', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('mobile_tel', models.CharField(blank=True, max_length=15, verbose_name='Mobile Phone', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('office_fax', models.CharField(blank=True, max_length=15, verbose_name='Office Fax', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('birthday', models.DateField(null=True, verbose_name='Birthday', blank=True)),
                ('note', models.TextField(verbose_name='Note', blank=True)),
                ('company', models.ForeignKey(blank=True, to='contact.CompanyLocation', null=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Contact Type',
                'verbose_name_plural': 'Contact Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso_code', models.CharField(max_length=2, serialize=False, verbose_name='ISO Code', primary_key=True)),
                ('name', models.CharField(max_length=45, verbose_name='Name')),
            ],
            options={
                'ordering': ['name', 'iso_code'],
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_type',
            field=models.ForeignKey(to='contact.ContactType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='company',
            name='company_type',
            field=models.ForeignKey(blank=True, to='contact.CompanyType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(to='contact.Country'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('address_line1', 'address_line2', 'postal_code', 'city', 'state_province', 'country')]),
        ),
    ]
