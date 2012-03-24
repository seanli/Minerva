import logging
from backstage.handler import DBLogHandler


class ExceptionMiddleware(object):

    def process_exception(self, request, exception):
        handler = DBLogHandler()
        logger = logging.getLogger('exception')
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.error(exception)
