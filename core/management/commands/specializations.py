import os
from django.utils import simplejson
from django.conf import settings
from core.models import Specialization
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):

    help = "Populates database with specializations."

    def handle_noargs(self, **options):
        programs = simplejson.load(open(os.path.join(settings.COMMANDS_ROOT[0], 'programs.json')))
        for program in programs['response']['data']['result']:
            new_specialization = Specialization()
            new_specialization.name = program['Name']
            new_specialization.save()
            print 'Added: %s' % program['Name']
