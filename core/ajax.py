from django.utils import simplejson
from dajaxice.decorators import dajaxice_register


def clear_validation(dajax, form, form_id):
    for field in form.fields:
        dajax.remove_css_class('div#%s-%s.control-group' % (form_id, field), 'error')
        dajax.assign('div#%s-%s.control-group .help-inline' % (form_id, field), 'innerHTML', '')
    dajax.remove_css_class('div#%s-error' % form_id, 'alert alert-error')
    dajax.assign('div#%s-error' % form_id, 'innerHTML', '')


def show_validation(dajax, form, form_id):
    for field, error in form.errors.items():
        if field != '__all__':
            dajax.add_css_class('div#%s-%s.control-group' % (form_id, field), 'error')
            dajax.assign('div#%s-%s.control-group .help-inline' % (form_id, field), 'innerHTML', error)
        else:
            dajax.add_css_class('div#%s-error' % form_id, 'alert alert-error')
            dajax.assign('div#%s-error' % form_id, 'innerHTML', error)


@dajaxice_register
def helloworld(request):
    return simplejson.dumps({'message': 'Hello World'})
