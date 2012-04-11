import os
from django.utils import simplejson
from django.conf import settings
from core.models import Skill
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):

    help = "Populates database with skills."

    def handle_noargs(self, **options):
        skills_1 = simplejson.load(open(os.path.join(settings.COMMANDS_ROOT[0], 'skills_1.json')))
        skills_2 = simplejson.load(open(os.path.join(settings.COMMANDS_ROOT[0], 'skills_2.json')))
        skills_3 = simplejson.load(open(os.path.join(settings.COMMANDS_ROOT[0], 'skills_3.json')))
        skills = list(set(skills_1 + skills_2 + skills_3))
        for skill in skills:
            new_skill = Skill()
            new_skill.name = skill
            new_skill.save()
            print 'Added: %s' % skill
