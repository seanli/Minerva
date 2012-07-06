from settings_base import *

ENVIRONMENT = 'PROD'

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'minerva',
        'USER': 'minerva',
        'PASSWORD': '1990106',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

COMPRESS_ENABLED = True
