from django import forms
from django.forms.util import ErrorList

class DivErrorList(ErrorList):
    
    def __unicode__(self):
        return self.as_divs()
    
    def as_divs(self):
        if not self: 
            return u''
        return u'<div class="errorlist">%s</div>' % u''.join([u'<div class="error">%s</div>' % e for e in self])