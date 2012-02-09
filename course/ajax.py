from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from Minerva.course.forms import AddCourseForm
from Minerva.core.models import Course
from Minerva.core.ajax import clear_validation, show_validation

@dajaxice_register
def form_add_course(request, form_data, form_id):
    dajax = Dajax()
    form = AddCourseForm(form_data)
    if form.is_valid():
        clear_validation(dajax, form, form_id)
        data = form.cleaned_data
        course = Course()
        course.name = data['name']
        course.abbrev = data['abbrev']
        course.institute = data['institute']
        course.save()
        # TODO: Adding new item will not update data-source
        dajax.add_data({'status': 'OK', 'new_item': course.name}, 'form_add_course_callback')
    else:
        clear_validation(dajax, form, form_id)
        show_validation(dajax, form, form_id)
    return dajax.json()
