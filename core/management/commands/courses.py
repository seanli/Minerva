import os
from django.utils import simplejson
from django.conf import settings
from course.models import Course
from core.models import Institute
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):

    help = "Populates database with courses."

    def handle_noargs(self, **options):
        courses = simplejson.load(open(os.path.join(settings.COMMANDS_ROOT[0], 'courses.json')))
        institute = Institute.objects.get(name='University of Waterloo')
        for course in courses['courses']:
            course = course['course']
            title = course['title']
            abbrev = course['faculty_acronym'] + ' ' + course['course_number']
            description = course['description']
            try:
                Course.objects.get(title=title)
            except Course.DoesNotExist:
                c = Course()
                c.title = title
                c.abbrev = abbrev
                c.institute = institute
                c.description = description
                c.save()
                print 'Added: %s' % c.abbrev
