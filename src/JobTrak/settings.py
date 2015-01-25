"""
Django settings for JobTrak project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wv9o)z07uyra13e4(c9d%6djiyjr$h7&b8y3&6z_+%r4m7+8(u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django_extensions',
    'jobtrak_core',
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
)

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj_jobtrak',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': '/opt/local/var/run/mariadb-10.0/mysqld.sock',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = "America/New_York"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR,'files','static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,'files','media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'files','templates'),
)
