from django.forms.util import ErrorList
from django import forms
from django.forms import ModelForm


class DivErrorList(ErrorList):

    def __unicode__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return u''
        return u'<div class="errorlist">%s</div>' % u''.join([u'<div class="error">%s</div>' % e for e in self])


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
