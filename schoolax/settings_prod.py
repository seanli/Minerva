from settings_base import *

ENVIRONMENT = 'PROD'

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lisean_minerva',
        'USER': 'lisean_minerva',
        'PASSWORD': '1990106',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = '/home/lisean/webapps/minerva_static/'
STATIC_URL = 'http://schoolax.com/static/'
MEDIA_ROOT = '/home/lisean/webapps/minerva_media/'
MEDIA_URL = 'http://schoolax.com/media/'

COMPRESS_ENABLED = True
