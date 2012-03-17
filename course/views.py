from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from creoleparser import text2html
from course.models import SectionAssign, Course
from django.utils.datastructures import SortedDict
from course.forms import AddCourseForm


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

    context = RequestContext(request)
    context['display'] = text2html("|=|=table|=header|\n|a|table|row|\n|b|table|row|")
    context['grouped_sections'] = grouped_sections
    context['form'] = form
    return render_to_response('homeroom/main.html', context)
