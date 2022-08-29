from .base import *

# SECURITY WARNING: don't run with debug turned on in production!

SECRET_KEY = 'django-insecure-cwd9bne^ytkj&r3fz4$zl3%v$tkoj#kejlo=0e+4s)x6yex=@@'


DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://*.herokuapp.com','https://*.127.0.0.1','https://obscure-citadel-20100.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dfoadlig4djejk',
        'USER': 'thlncfphojsvdh',
        'PASSWORD': '9bc165ede3da270773a33eab5bec75f224bd5dcfbcd388623f60da2273139f50',
        'HOST': 'ec2-3-223-242-224.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


import django_heroku
django_heroku.settings(locals())