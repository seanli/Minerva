from settings_base import *

ENVIRONMENT = 'QA'

DEBUG = False
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lisean_minerva_qa',
        'USER': 'lisean_minerva_qa',
        'PASSWORD': '1990106',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = '/home/lisean/webapps/minerva_static/'
STATIC_URL = 'http://schoolax.com/static/'
MEDIA_ROOT = '/home/lisean/webapps/minerva_media/'
MEDIA_URL = 'http://schoolax.com/media/'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://qa.schoolax.com/solr/',
        'TIMEOUT': 60 * 5,
        'INCLUDE_SPELLING': True,
    },
}

COMPRESS_ENABLED = True
