from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from course.models import Course


@login_required
def courses(request, course_id=None):
    context = RequestContext(request)
    try:
        course_obj = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        course_obj = None
    if course_obj is not None:
        context['course'] = course_obj
        return render_to_response('course/course_detail.html', context)
    else:
        return HttpResponse('Course Not Found!')
