from settings_base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'minerva',
        'USER': 'minerva_admin',
        'PASSWORD': '1990106',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
