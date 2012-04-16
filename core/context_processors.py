from django.conf import settings as django_settings
from backstage.forms import ReportForm
import logging


def settings(request):
    '''
    Adds the settings specified in settings.TEMPLATE_VISIBLE_SETTINGS to the request context.
    '''
    context = {}
    for attr in django_settings.TEMPLATE_VISIBLE_SETTINGS:
        try:
            context[attr] = getattr(django_settings, attr)
        except AttributeError:
            context[attr] = None
            msg = 'TEMPLATE_VISIBLE_SETTINGS: "%s" does not exist.' % format(attr)
            exception_logger = logging.getLogger('minerva')
            exception_logger.warning(msg)
    return context


def global_forms(request):
    '''
    Adds global forms to the request context
    '''
    context = {}
    context['report_form'] = ReportForm()
    return context
