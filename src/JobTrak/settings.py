"""
Django settings for jobtrak project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR=os.path.dirname(os.path.dirname(__file__))

SECRET_KEY='wv9o)z07uyra13e4(c9d%6djiyjr$h7&b8y3&6z_+%r4m7+8(u'

DEBUG=True

TEMPLATE_DEBUG=True

ALLOWED_HOSTS=[]

INSTALLED_APPS=(
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'bootstrap3',
    'mmg.jobtrak.util',
    'mmg.jobtrak.core',
    'mmg.jobtrak.contact',
    'mmg.jobtrak.links',
    'mmg.jobtrak.cms',
    'mmg.jobtrak.public',
    'mmg.jobtrak.help',
)

ROOT_URLCONF='JobTrak.urls'

WSGI_APPLICATION='JobTrak.wsgi.application'

MIDDLEWARE_CLASSES=(
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

GRAPH_MODELS={
    'all_applications': True,
    'group_models': True,
}
BOOTSTRAP3={
    # The URL to the jQuery JavaScript file
    'jquery_url': '//code.jquery.com/jquery.min.js',

    # The Bootstrap base URL
    'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.3.1/',

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': None,

    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': None,

    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    'javascript_in_head': False,

    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    'include_jquery': False,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-2',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-4',

    # Set HTML required attribute on required fields
    'set_required': True,

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'has-error',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'has-success',

    # Renderers (only set these if you have studied the source and understand the inner workings)
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

TEMPLATE_CONTEXT_PROCESSORS=(
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.debug',
    'django.contrib.messages.context_processors.messages',
)


DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj_jobtrak',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': '/opt/local/var/run/mariadb-10.0/mysqld.sock',
    }
}

TIME_ZONE='America/New_York'
USE_TZ=True

USE_L10N=True
USE_THOUSAND_SEPARATOR=True

USE_I18N=True
LANGUAGE_CODE='en-us'
LANGUAGE_COOKIE_NAME='jobtrak_linga'
ugettext=lambda s: s
LANGUAGES = (
    ('en', ugettext('English')),
    ('de', ugettext('German')),
    ('tr', ugettext('Turkish')),
    ('es', ugettext('Spanish')),
)

LOCALE_PATHS=(
    os.path.join(BASE_DIR,'files','locale'),
)

STATICFILES_DIRS=(
    ('libs',os.path.join(BASE_DIR,'libs')),
)

STATICFILES_FINDERS=(
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT=os.path.join(BASE_DIR,'files','static')
STATIC_URL='/static/'

MEDIA_ROOT=os.path.join(BASE_DIR,'files','media')
MEDIA_URL='/media/'

TEMPLATE_DIRS=(
    os.path.join(BASE_DIR,'files','templates'),
)
