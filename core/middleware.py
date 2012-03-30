import logging
from backstage.handler import DBLogHandler


# Updates existing loggers

db_handler = DBLogHandler()
db_handler.setLevel(logging.DEBUG)

django_logger = logging.getLogger('django')
django_logger.addHandler(db_handler)

dajaxice_logger = logging.getLogger('dajaxice')
dajaxice_logger.addHandler(db_handler)

minerva_logger = logging.getLogger('minerva')
minerva_logger.addHandler(db_handler)

backup_logger = logging.getLogger('backup')


class ExceptionMiddleware(object):

    def process_exception(self, request, exception):
        exception_db_handler = DBLogHandler(request=request)
        exception_logger = logging.getLogger('exception')
        exception_logger.setLevel(logging.WARNING)
        exception_logger.addHandler(exception_db_handler)
        exception_logger.propagate = True
        try:
            exception_logger.error(exception)
        except:
            backup_logger.error(exception)
