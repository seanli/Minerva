from django.contrib.sessions.models import Session
from django.contrib.admin.models import LogEntry
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):

    help = 'Cleans admin log entries and session data.'

    def handle_noargs(self, **options):
        sessions = Session.objects.all()
        counter = 0
        for session in sessions:
            session.delete()
            counter += 1
        print '%s session(s) deleted.' % counter
        counter = 0
        admin_logs = LogEntry.objects.all()
        for admin_log in admin_logs:
            admin_log.delete()
            counter += 1
        print '%s admin log(s) deleted.' % counter
