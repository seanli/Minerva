from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.utils import simplejson
from homeroom.forms import AddCourseForm
from course.models import Section, SectionAssign
from core.ajax import clear_validation, show_validation


@dajaxice_register
def form_add_course(request, form_data, form_id):
    dajax = Dajax()
    form = AddCourseForm(form_data, request=request)
    if form.is_valid():
        clear_validation(dajax, form, form_id)
        data = form.cleaned_data
        section = data.get('section', '')
        if section == '':
            section = Section()
            section.course = data['course']
            section.start_date = data['start_date']
            section.duration = data['duration']
            section.save()
        profile = request.user.get_profile()
        profile.add_section(section)
        dajax.add_data({'status': 'OK'}, 'form_add_course_callback')
    else:
        clear_validation(dajax, form, form_id)
        show_validation(dajax, form, form_id)
        dajax.add_data({'status': 'INVALID'}, 'form_add_course_callback')
    return dajax.json()


@dajaxice_register
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
