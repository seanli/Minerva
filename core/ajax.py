from django.utils import simplejson
from dajaxice.decorators import dajaxice_register


def clear_validation(dajax, form):
    for field in form.fields:
        dajax.remove_css_class('div[row="%s"].control-group' % field, 'error')
        dajax.assign('div[row="%s"].control-group .help-inline' % field, 'innerHTML', '')
    dajax.remove_css_class('div[row="error"]', 'alert alert-error')
    dajax.assign('div[row="error"]', 'innerHTML', '')


def show_validation(dajax, form):
    for field, error in form.errors.items():
        if field != '__all__':
            dajax.add_css_class('div[row="%s"].control-group' % field, 'error')
            dajax.assign('div[row="%s"].control-group .help-inline' % field, 'innerHTML', error)
        else:
            dajax.add_css_class('div[row="error"]', 'alert alert-error')
            dajax.assign('div[row="error"]', 'innerHTML', error)


@dajaxice_register
def helloworld(request):
    return simplejson.dumps({'message': 'Hello World'})
