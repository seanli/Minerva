from django import forms
from django.forms import ModelChoiceField
from Minerva.core.forms import DivErrorList
from Minerva.core.models import Institute, Course, Profile
from Minerva.core.utilities import titlecase
import datetime

class AddCourseForm(forms.Form):
    
    class InstructorChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return obj.user.get_full_name()
    
    name = forms.CharField(max_length=100, label='Course Name', widget=forms.TextInput(attrs={'data-provide':'typeahead', 'data-items':'4', 'autocomplete':'off', 'data-source':"[]"}))
    institute = forms.ModelChoiceField(queryset=Institute.objects, label='Institute')
    first_day = forms.DateField(label='First Day', initial=datetime.datetime.today().strftime('%m/%d/%Y'), widget=forms.DateInput(attrs={'data-datepicker':'datepicker'}))
    last_day = forms.DateField(label='Last Day', initial=datetime.datetime.today().strftime('%m/%d/%Y'), widget=forms.DateInput(attrs={'data-datepicker':'datepicker'}))
    instructor = InstructorChoiceField(queryset=Profile.objects.filter(role='I'), label='Instructor')
    
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
    
    def clean(self):
        data = self.cleaned_data
        name = data.get('name', '')
        institute = data.get('institute', '')
        if name != '' and institute != '' and Course.objects.filter(name__icontains=name, institute=institute).count() == 0:
            raise forms.ValidationError('<strong>%s</strong> for <strong>%s</strong> is not a registered course!' % (name, institute))
        elif name != '' and institute != '':
            data['course'] = Course.objects.filter(name__icontains=name, institute=institute)[0]
            return data
        else:
            return data