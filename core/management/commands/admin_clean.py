from django.core.management.base import NoArgsCommand
from core.management.commands.utilities import class_clean


class Command(NoArgsCommand):

    help = 'Cleans admin log entries and session data.'

    def handle_noargs(self, **options):
        classes = ['Session', 'LogEntry', 'LogMessage']
        # Cleans data
        class_clean(classes)
