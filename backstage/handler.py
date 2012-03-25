import sys
import traceback
import logging
from backstage.models import LogMessage
from datetime import datetime


class DBLogHandler(logging.Handler):

    def __init__(self, request=None):
        logging.Handler.__init__(self)
        self.request = request

    def emit(self, record):
        log_message = LogMessage()
        log_message.logger_name = record.name
        log_message.logged_time = datetime.now()
        log_message.level = record.levelno
        log_message.file_path = record.pathname
        log_message.function_name = record.funcName
        log_message.line_number = record.lineno
        if len(record.args) > 0:
            log_message.message = record.message
        else:
            log_message.message = record.msg
        log_message.traceback = self.get_traceback()
        if self.request is not None:
            abs_uri = self.request.build_absolute_uri(self.request.get_full_path())
            log_message.uri_path = abs_uri
            log_message.request = self.request
            if self.request.user.is_authenticated():
                log_message.user = self.request.user
        log_message.save()

    def get_traceback(self):
        exc_type, exc_value, exc_tb = sys.exc_info()
        return '\n'.join(traceback.format_exception(exc_type, exc_value, exc_tb))
