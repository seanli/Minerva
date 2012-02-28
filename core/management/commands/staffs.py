import os
from django.utils import simplejson
from django.conf import settings
from django.contrib.auth.models import User
from Minerva.core.models import Profile, Institute
from Minerva.core.utilities import unique_username
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):

    help = "Populates database with staffs."

    def handle_noargs(self, **options):
        staffs = simplejson.load(open(os.path.join(settings.COMMANDS_ROOT[0], 'staffs.json')))
        institute = Institute.objects.get(name='University of Waterloo')
        for staff in staffs:
            try:
                user = User()
                user.username = unique_username(staff['firstName'], staff['lastName'])
                user.email = staff['userID'] + '@uwaterloo.ca'
                user.set_password(staff['userID'])
                user.first_name = staff['firstName']
                user.last_name = staff['lastName']
                user.is_active = False
                user.save()
                profile = Profile()
                profile.user = user
                profile.institute = institute
                profile.role = 'I'
                profile.save()
                print 'Added %s.' % staff['userID']
            except:
                pass
