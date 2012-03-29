from account.models import Profile
from core.models import Institute
from django.contrib.auth.models import User
from django.core.management.base import NoArgsCommand
from core.management.commands.utilities import class_clean


class Command(NoArgsCommand):

    help = 'Resets database with essential data.'

    def handle_noargs(self, **options):
        classes = ['User', 'Group', 'Wiki', 'Ticket', 'Badge', 'Section',
            'Review', 'Session', 'LogEntry', 'LogMessage']
        # Cleans data
        class_clean(classes)
        # Creates superuser
        user = User()
        user.username = 'admin'
        user.email = 'admin@schoolax.com'
        user.set_password('1990106')
        user.first_name = 'Admin'
        user.last_name = 'Schoolax'
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        profile = Profile()
        profile.user = user
        profile.institute = Institute.objects.get(name='University of Waterloo')
        profile.role = 'S'
        profile.save()
        print 'Superuser is created.'
        print 'Email: admin@schoolax.com'
        print 'Password: 1990106'
