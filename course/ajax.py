from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from course.forms import AddCourseForm
from core.models import Section
from Minerva.core.ajax import clear_validation, show_validation


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
            section.first_day = data['first_day']
            section.last_day = data['last_day']
            section.instructor = data['instructor']
            section.save()
        profile = request.user.get_profile()
        profile.add_section(section)
        # TODO: Adding new item will not update data-source
        dajax.add_data({'status': 'OK'}, 'form_add_course_callback')
    else:
        clear_validation(dajax, form, form_id)
        show_validation(dajax, form, form_id)
        dajax.add_data({'status': 'INVALID'}, 'form_add_course_callback')
    return dajax.json()
