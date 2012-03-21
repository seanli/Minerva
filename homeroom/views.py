from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from creoleparser import text2html
from course.models import SectionAssign, Course
from django.utils.datastructures import SortedDict
from course.forms import AddCourseForm
from django.utils import simplejson
from django.db.models import Q


@login_required
def homeroom(request):
    user = request.user
    sections = [assign.section for assign in SectionAssign.objects.filter(user=user).order_by('-section__start_date')]
    grouped_sections = SortedDict()
    for section in sections:
        start_date = section.start_date
        if start_date not in grouped_sections:
            grouped_sections[start_date] = [section]
        else:
            grouped_sections[start_date].append(section)
    for key, value in grouped_sections.items():
        grouped_sections[key] = sorted(value, key=lambda s: s.course.title)

    form = AddCourseForm(request=request)

    context = RequestContext(request)
    context['display'] = text2html("|=|=table|=header|\n|a|table|row|\n|b|table|row|")
    context['grouped_sections'] = grouped_sections
    context['form'] = form
    return render_to_response('homeroom/main.html', context)


@login_required
def source_course(request):
    json = []
    if 'term' in request.GET:
        term = request.GET['term']
        courses = Course.objects.filter(Q(title__icontains=term) | Q(abbrev__icontains=term)).order_by('title')[:7]
        for course in courses:
            datum = {}
            datum['title'] = course.title
            datum['abbrev'] = course.abbrev
            datum['value'] = course.id
            json.append(datum)
    return HttpResponse(simplejson.dumps(json))
