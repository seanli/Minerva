from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse
from course.models import SectionAssign, Section
from django.utils.datastructures import SortedDict
from homeroom.forms import AddCourseForm


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
    context['grouped_sections'] = grouped_sections
    context['form'] = form
    return render_to_response('homeroom/main.html', context)


@login_required
def class_section(request, section_id=None):
    context = RequestContext(request)
    try:
        section_obj = Section.objects.get(id=section_id)
    except Section.DoesNotExist:
        section_obj = None
    if section_obj is not None:
        classmates = [assign.user for assign in SectionAssign.objects.filter(section=section_obj)]
        context['section'] = section_obj
        context['classmates'] = classmates
        return render_to_response('homeroom/class.html', context)
    else:
        return HttpResponse('Section Not Found!')
