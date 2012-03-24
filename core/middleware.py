import sys
import logging
import traceback
from backstage.handler import DBLogHandler


# Updates existing loggers

handler = DBLogHandler()
handler.setLevel(logging.DEBUG)

django_logger = logging.getLogger('django')
django_logger.addHandler(handler)

dajaxice_logger = logging.getLogger('dajaxice')
dajaxice_logger.addHandler(handler)

minerva_logger = logging.getLogger('minerva')
minerva_logger.addHandler(handler)

# Exception logger

exception_logger = logging.getLogger('exception')
exception_logger.setLevel(logging.WARNING)
exception_logger.addHandler(handler)
exception_logger.propagate = True


class ExceptionMiddleware(object):

    def process_exception(self, request, exception):
        message = "%s\n\n%s" % (_get_traceback(exception), repr(request))
        minerva_logger.debug('DAFUQ')
        exception_logger.error(message)


def _get_traceback(self, exception=None):
    '''
    Helper function to return the traceback as a string
    '''
    return '\n'.join(traceback.format_exception(*(exception or sys.exc_info())))
