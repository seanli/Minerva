from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from Minerva.course.forms import AddCourseForm
from Minerva.core.models import Section, SectionAssign
from Minerva.core.ajax import clear_validation, show_validation

@dajaxice_register
def form_add_course(request, form_data, form_id):
    try:
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
            assign = SectionAssign()
            assign.section = section
            assign.profile = request.user.get_profile()
            assign.save()
            # TODO: Adding new item will not update data-source
            dajax.add_data({'status': 'OK', 'new_item': 'lol'}, 'form_add_course_callback')
        else:
            clear_validation(dajax, form, form_id)
            show_validation(dajax, form, form_id)
        return dajax.json()
    except Exception, e:
        print e
