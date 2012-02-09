from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from Minerva.core.models import BadgeAssign, Section, SectionAssign
from datetime import datetime
from Minerva.course.forms import AddCourseForm

@login_required
def home(request):
    profile = request.user.get_profile()
    badges = BadgeAssign.objects.filter(profile=profile)
    sections = SectionAssign.objects.filter(profile=profile, section__first_day__lte=datetime.today(), section__last_day__gte=datetime.today())
    form = AddCourseForm()
    data = {
        'badges': badges,
        'sections': sections,
        'form': form,
    }
    return render_to_response('home.html', data, context_instance=RequestContext(request))