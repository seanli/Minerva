from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from Minerva.core.models import SectionAssign, Course
from datetime import datetime
from Minerva.course.forms import AddCourseForm


@login_required
def bulletin(request):
    user = request.user
    sections = SectionAssign.objects.filter(user=user, section__first_day__lte=datetime.today(), section__last_day__gte=datetime.today())
    source = ''
    courses = Course.objects.filter(institute=user.get_profile().institute).order_by('title')
    last = len(courses) - 1
    index = 0
    for course in courses:
        if (index != last):
            source += '"%s",' % (course.title)
        else:
            source += '"%s"' % (course.title)
        index += 1
    source = '[' + source + ']'

    form = AddCourseForm(request=request, source=source)

    context = {
        'sections': sections,
        'courses': courses,
        'form': form,
    }
    return render_to_response('bulletin.html', context, context_instance=RequestContext(request))
