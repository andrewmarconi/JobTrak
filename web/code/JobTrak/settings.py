# -*- coding: utf-8
"""
Django settings for jobtrak project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'wv9o)z07uyra13e4(c9d%6djiyjr$h7&b8y3&6z_+%r4m7+8(u'

DEBUG = True

# TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
	'grappelli',
	'django.contrib.admin',
#	'django.contrib.admin.apps.SimpleAdminConfig',
	'django.contrib.admindocs',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.humanize',
	'django_extensions',
	'bootstrap3',
	'taggit',
	'django_tables2',
	'external_urls',
	'mmg.jobtrak.util',
	'mmg.jobtrak.core',
	'mmg.jobtrak.links',
	'mmg.jobtrak.contact',
	'mmg.jobtrak.cms',
	'mmg.jobtrak.public',
	'mmg.jobtrak.profile',
	'mmg.jobtrak.help',
)

ROOT_URLCONF = 'JobTrak.urls'

WSGI_APPLICATION = 'JobTrak.wsgi.application'

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.contrib.admindocs.middleware.XViewMiddleware',
	'django.middleware.locale.LocaleMiddleware',
)

BOOTSTRAP3 = {
	'jquery_url': '//code.jquery.com/jquery.min.js',
	'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.3.1/',
	'css_url': None,
	'theme_url': None,
	'javascript_url': None,
	'javascript_in_head': False,
	'include_jquery': False,
	'horizontal_label_class': 'col-md-2',
	'horizontal_field_class': 'col-md-4',
	'set_required': True,
	'set_placeholder': True,
	'required_css_class': '',
	'error_css_class': 'has-error',
	'success_css_class': 'has-success',
	'formset_renderers':{
		'default': 'bootstrap3.renderers.FormsetRenderer',
	},
	'form_renderers': {
		'default': 'bootstrap3.renderers.FormRenderer',
	},
	'field_renderers': {
		'default': 'bootstrap3.renderers.FieldRenderer',
		'inline': 'bootstrap3.renderers.InlineFieldRenderer',
	},
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'files','templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

USE_THOUSAND_SEPARATOR = True

# LANGUAGE_COOKIE_NAME = 'jobtrak_l'
# CSRF_COOKIE_NAME = 'jobtrak_c'
# SESSION_COOKIE_NAME = 'jobtrak_s'

GRAPPELLI_ADMIN_TITLE = "JobTrak"
GRAPPELLI_AUTOCOMPLETE_LIMIT = 10
GRAPPELLI_SWITCH_USER = True

ugettext = lambda s: s

LANGUAGES  =  (
	('de', u'Deutsch'),
	('nl', u'Dutch'),
	('en', u'English'),
	('es', u'Español'),
	('fi', u'Finnish'),
	('fr', u'Français'),
	('it', u'Italian'),
	('sv', u'Swedish'),
	('tr', u'Türkçe'),
)

LOCALE_PATHS = (
	os.path.join(BASE_DIR,'files','locale'),
	os.path.join(BASE_DIR,'mmg','jobtrak','cms'),
	os.path.join(BASE_DIR,'mmg','jobtrak','contact'),
	os.path.join(BASE_DIR,'mmg','jobtrak','core'),
	os.path.join(BASE_DIR,'mmg','jobtrak','help'),
	os.path.join(BASE_DIR,'mmg','jobtrak','links'),
	os.path.join(BASE_DIR,'mmg','jobtrak','profile'),
	os.path.join(BASE_DIR,'mmg','jobtrak','public'),
	os.path.join(BASE_DIR,'mmg','jobtrak','util'),
)


STATICFILES_DIRS = (
	('libs',os.path.join(BASE_DIR,'libs')),
)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = os.path.join(BASE_DIR,'files','static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,'files','media')
MEDIA_URL = '/media/'
