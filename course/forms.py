from django import forms
from Minerva.core.forms import DivErrorList
from Minerva.core.models import Institute, Course
from Minerva.core.utilities import titlecase 

class AddCourseForm(forms.Form):
    
    name = forms.CharField(max_length=100, label='Course Name', widget=forms.TextInput(attrs={'data-provide':'typeahead', 'data-items':'4', 'autocomplete':'off', 'data-source':"[]"}))
    abbrev = forms.CharField(max_length=10, label='Abbreviation')
    institute = forms.ModelChoiceField(queryset=Institute.objects, empty_label=None, label='Institute')
    
    def __init__(self, *args, **kwargs):
        try:
            source = kwargs.pop('source')
        except:
            source = "[]"
        super(AddCourseForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList
        self.fields["name"].widget = forms.TextInput(attrs={'data-provide':'typeahead', 'data-items':'4', 'autocomplete':'off', 'data-source':source})
        
    def clean_name(self):
        name = titlecase(self.cleaned_data["name"].strip())
        return name
    
    def clean_abbrev(self):
        abbrev = self.cleaned_data["abbrev"].upper().strip()
        return abbrev
    
    def clean(self):
        data = self.cleaned_data
        name = data.get('name', '').strip()
        institute = data['institute']
        try:
            Course.objects.get(name=name, institute=institute)
        except Course.DoesNotExist:
            return data
        raise forms.ValidationError('This course for <strong>%s</strong> already exists!' % institute)