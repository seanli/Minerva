from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from core.forms import make_row_name


def clear_validation(dajax, form):
    for field in form.fields:
        dajax.remove_css_class('div[row="%s"].control-group' % make_row_name(form, field), 'error')
        dajax.assign('div[row="%s"].control-group .help-inline' % make_row_name(form, field), 'innerHTML', '')
    dajax.remove_css_class('div[row="%s"]' % make_row_name(form, 'error'), 'alert alert-error')
    dajax.assign('div[row="%s"]' % make_row_name(form, 'error'), 'innerHTML', '')


def show_validation(dajax, form):
    for field, error in form.errors.items():
        if field != '__all__':
            dajax.add_css_class('div[row="%s"].control-group' % make_row_name(form, field), 'error')
            dajax.assign('div[row="%s"].control-group .help-inline' % make_row_name(form, field), 'innerHTML', error)
        else:
            dajax.add_css_class('div[row="%s"]' % make_row_name(form, 'error'), 'alert alert-error')
            dajax.assign('div[row="%s"]' % make_row_name(form, 'error'), 'innerHTML', error)


@dajaxice_register
def helloworld(request):
    return simplejson.dumps({'message': 'Hello World'})
