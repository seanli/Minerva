from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from Minerva.core.models import BadgeAssign, Section, SectionAssign, Course
from datetime import datetime
from Minerva.course.forms import AddCourseForm

@login_required
def home(request):
    profile = request.user.get_profile()
    badges = BadgeAssign.objects.filter(profile=profile)
    sections = SectionAssign.objects.filter(profile=profile, section__first_day__lte=datetime.today(), section__last_day__gte=datetime.today())
    
    source = ''
    courses = Course.objects.filter(institute=profile.institute)
    last = len(courses) - 1
    index = 0
    for course in courses:
        if (index != last):
            source += '"%s",' % course.name
        else:
            source += '"%s"' % course.name
        index += 1
    source = '[' + source + ']'
    
    form = AddCourseForm(request=request, source=source)
    
    data = {
        'badges': badges,
        'sections': sections,
        'courses': courses,
        'form': form,
    }
    return render_to_response('home.html', data, context_instance=RequestContext(request))