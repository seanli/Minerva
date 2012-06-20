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


def make_row_name(form, name):
    return form.__class__.__name__ + '-' + name


def as_standard(self):
    output = []
    for name, field in self.fields.items():
        name_field = self[name]
        if field.__class__ == GenericField or name_field.is_hidden:
            output.append(unicode(name_field))
        else:
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
    for name, field in self.fields.items():
        name_field = self[name]
        if field.__class__ == GenericField or name_field.is_hidden:
            output.append(unicode(name_field))
        else:
            control_group = '<div row="%s" class="control-group">%s</div>'
            label = '<label for="id_%s" class="control-label">%s</label>' % (name, name_field.label)
            control = '<div class="controls">%s<span class="help-inline"></span></div>' % (name_field)
            control_group = control_group % (make_row_name(self, name_field.html_name), label + control)
            output.append(control_group)
    output.append('<div row="%s"></div>' % make_row_name(self, 'error'))
    return mark_safe(u'\n'.join(output))


def as_landing(self):
    output = []
    errors = []
    for name, field in self.fields.items():
        name_field = self[name]
        if field.__class__ == GenericField or name_field.is_hidden:
            output.append(unicode(name_field))
        else:
            if name_field.errors:
                field_group = '<div class="field error">%s</div>'
            else:
                field_group = '<div class="field">%s</div>'
            label = '<label for="id_%s">%s</label>' % (name, name_field.label)
            if name_field.errors:
                field_input = '%s<span class="help-inline">%s</span>' % (name_field, name_field.errors)
            else:
                field_input = '%s' % (name_field)
            field_group = field_group % (label + field_input)
            output.append(field_group)
    if len(errors) > 0:
        output.append('div class="error">%s</div>' % u'<br />'.join(errors))
    print output
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
StandardForm.as_landing = as_landing


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


class GenericField(forms.Field):

    def __init__(self, required=False, widget=None):
        super(GenericField, self).__init__(required, widget)


class LegendWidget(forms.Widget):

    def __init__(self, attrs=None):
        default_attrs = {'display': 'Legend'}
        if attrs:
            default_attrs.update(attrs)
        super(LegendWidget, self).__init__(default_attrs)

    def __unicode__(self):
        return self.render()

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe('<legend>%s</legend>' % final_attrs['display'])
