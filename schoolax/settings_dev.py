from settings_base import *

ENVIRONMENT = 'DEV'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DAJAXICE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'minerva',
        'USER': 'minerva_admin',
        'PASSWORD': '1990106',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

COMPRESS_ENABLED = False

# Render CSS Using LESS (Slower)

USE_LESS = False

if USE_LESS:
    TEMPLATE_VISIBLE_SETTINGS += (
        'USE_LESS',
    )

# Swap User Feature

SWAP_USER = True

if SWAP_USER:
    TEMPLATE_VISIBLE_SETTINGS += (
        'SWAP_USER',
    )

# Django Debug Toolbar

ENABLE_TOOLBAR = False

if ENABLE_TOOLBAR:

    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS += (
        'debug_toolbar',
    )

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.profiling.ProfilingDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.cache.CacheDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )

    def toolbar_callback(request):
        return ENABLE_TOOLBAR

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': True,
        'SHOW_TOOLBAR_CALLBACK': toolbar_callback,
        'ENABLE_STACKTRACES': True,
    }
