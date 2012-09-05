from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse
from course.models import Course, SectionAssign, Section, WhiteboardPost
# from django.utils.datastructures import SortedDict
from homeroom.forms import AddCourseForm, AddWhiteboardPostForm
from haystack.query import SearchQuerySet
from haystack.utils import Highlighter


@login_required
def homeroom(request):
    user = request.user
    context = RequestContext(request)
    if request.method == 'POST':
        query = request.POST['course-search']
        results = SearchQuerySet().autocomplete(text=query).models(Course)[:10]
        highlighter = Highlighter(query, html_tag='span', css_class='keyword')
        courses = []
        for result in results:
            course = {}
            course['object'] = result.object
            course['highlight'] = highlighter.highlight(result.text)
            courses.append(course)
        # courses = Course.objects.filter(institute=user.get_profile().institute, title__icontains=query)
        suggestion = None
        # suggestion = SearchQuerySet().spelling_suggestion(query)
        context['courses'] = courses
        context['suggestion'] = suggestion
    sections = [assign.section for assign in SectionAssign.objects.filter(user=user).order_by('-section__start_date')]
    form = AddCourseForm(request=request)
    context['sections'] = sections
    context['form'] = form
    return render_to_response('homeroom/index.html', context)


@login_required
def class_section(request, section_id=None):
    context = RequestContext(request)
    try:
        section_obj = Section.objects.get(id=section_id)
    except Section.DoesNotExist:
        section_obj = None
    if section_obj is not None:
        classmates = [assign.user for assign in SectionAssign.objects.filter(section=section_obj)]
        posts = WhiteboardPost.objects.filter(section=section_obj).order_by('-created_time')
        context['section'] = section_obj
        context['classmates'] = classmates
        context['posts'] = posts
        context['post_form'] = AddWhiteboardPostForm(request=request)
        return render_to_response('homeroom/class.html', context)
    else:
        return HttpResponse('Section Not Found!')
