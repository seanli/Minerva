from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from homeroom.forms import AddCourseForm, AddWhiteboardPostForm
from course.models import Section, SectionAssign, WhiteboardPost
from core.ajax import clear_validation, show_validation


@dajaxice_register
@login_required
def form_add_course(request, form_data):
    dajax = Dajax()
    callback = 'form_add_course_callback'
    form = AddCourseForm(form_data, request=request)
    if form.is_valid():
        clear_validation(dajax, form)
        data = form.cleaned_data
        section = data.get('section', None)
        if section == None:
            section = Section()
            section.course = data['course']
            section.start_date = data['start_date']
            section.duration = data['duration']
            section.save()
        user = request.user
        user.add_section(section)
        dajax.add_data({'status': 'OK'}, callback)
    else:
        show_validation(dajax, form)
        dajax.add_data({'status': 'INVALID'}, callback)
    return dajax.json()


@dajaxice_register
@login_required
def form_whiteboard_post(request, form_data):
    dajax = Dajax()
    callback = 'form_whiteboard_post_callback'
    form = AddWhiteboardPostForm(form_data, request=request)
    if form.is_valid():
        clear_validation(dajax, form)
        data = form.cleaned_data
        content = data['content']
        section = data['section']
        post = WhiteboardPost()
        post.content = content
        post.author = request.user
        post.section = section
        post.save()
        dajax.add_data({'status': 'OK'}, callback)
    else:
        show_validation(dajax, form)
        dajax.add_data({'status': 'INVALID'}, callback)
    return dajax.json()


@dajaxice_register
@login_required
def unsubscribe_section(request, section_id):
    try:
        section = Section.objects.get(pk=section_id)
        user = request.user
        assign = SectionAssign.objects.get(user=user, section=section)
        assign.delete()
        status = 'OK'
    except:
        status = 'INVALID'
    return simplejson.dumps({'status': status})
