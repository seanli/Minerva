import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = PROJECT_ROOT.split(os.sep)[-1]

ADMINS = (
    ('Sean Li', 'lishang106@gmail.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
USE_TZ = True
TIME_ZONE = 'America/Tijuana'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and calendars according to the current locale
USE_L10N = True

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'assets'),
)

# List of finder classes that know how to find static files in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(@7*5s+@kqh*-^622sg2=5^l&y#0kl()72%!dp*om###jlkmdl'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'core.middleware.ExceptionMiddleware',
)

ROOT_URLCONF = '%s.urls' % PROJECT_DIR

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'fixtures'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.webdesign',
    'south',
    'haystack',
    'dajaxice',
    'dajax',
    'creoleparser',
    'compressor',
    'core',
    'core.templatetags',
    'core.management',
    'core.management.commands',
    'backstage',
    'course',
    'account',
    'bulletin',
    'homeroom',
    'portfolio',
    'data',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'core.context_processors.settings',
    'core.context_processors.global_forms',
)

# For core.context_processors.settings
TEMPLATE_VISIBLE_SETTINGS = (
    'DEBUG',
    'BRAND_NAME',
    'ENVIRONMENT',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(name)s - %(levelname)s - %(asctime)s: %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_ROOT, 'logs/minerva.log'),
            'maxBytes': '16777216',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'minerva': {
            'level': 'DEBUG',
            'propagate': True,
        },
        'dajaxice': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'backup': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        }
    }
}

AUTH_PROFILE_MODULE = 'account.Profile'
AUTHENTICATION_BACKENDS = ('account.backends.EmailAuthBackend',)
LOGIN_URL = '/login/'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(PROJECT_ROOT, 'indexes'),
        'INCLUDE_SPELLING': True,
    },
}

DAJAXICE_MEDIA_PREFIX = 'dajaxice'
DAJAXICE_JS_DOCSTRINGS = True

COMMANDS_ROOT = os.path.join(PROJECT_ROOT, 'core/management/commands/'),

BRAND_NAME = 'Schoolax'
