from django.forms.util import ErrorList
from django import forms
from django.utils.safestring import mark_safe
from django.forms import ModelForm


class DivErrorList(ErrorList):

    def __unicode__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return u''
        return u'<div class="errorlist">%s</div>' % u''.join([u'<div class="error">%s</div>' % e for e in self])


def as_standard(self):
    output = []
    for name, _ in self.fields.items():
        name_field = self[name]
        if name_field.errors:
            control_group = '<div class="control-group error">%s</div>'
        else:
            control_group = '<div class="control-group">%s</div>'
        label = '<label for="id_%s" class="control-label">%s</label>' % (name, name_field.label)
        control = '<div class="controls">%s<span class="help-inline">%s</span></div>' % (name_field, name_field.errors)
        control_group = control_group % (label + control)
        output.append(control_group)
    return mark_safe(u'\n'.join(output))

            
def as_standard_ajax(self):
    output = []
    for name, _ in self.fields.items():
        name_field = self[name]
        control_group = '<div row="%s" class="control-group">%s</div>'
        label = '<label for="id_%s" class="control-label">%s</label>' % (name, name_field.label)
        control = '<div class="controls">%s<span class="help-inline"></span></div>' % (name_field)
        control_group = control_group % (name_field.html_name, label + control)
        output.append(control_group)
    output.append('<div row="error"></div>')
    return mark_safe(u'\n'.join(output))

    
class StandardForm(forms.Form):

    def __init__(self, *args, **kwargs):
        try:
            # A request parameter can be passed
            self.request = kwargs.pop('request')
        except:
            self.request = None
        super(StandardForm, self).__init__(*args, **kwargs)
        # Set default error list display
        self.error_class = DivErrorList

StandardForm.as_standard = as_standard
StandardForm.as_standard_ajax = as_standard_ajax


class StandardModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        try:
            # A request parameter can be passed
            self.request = kwargs.pop('request')
        except:
            self.request = None
        super(StandardModelForm, self).__init__(*args, **kwargs)
        # Set default error list display
        self.error_class = DivErrorList

StandardModelForm.as_standard = as_standard
StandardModelForm.as_standard_ajax = as_standard_ajax
