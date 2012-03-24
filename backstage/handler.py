import logging
from backstage.models import LogMessage


class DBLogHandler(logging.Handler):

    def emit(self, record):
        log_message = LogMessage()
        log_message.logger_name = record.name
        log_message.level = record.levelno
        log_message.file_path = record.pathname
        log_message.function_name = record.funcName
        log_message.line_number = record.lineno
        if len(record.args) > 0:
            log_message.message = record.message
        else:
            log_message.message = record.msg
        log_message.save()
