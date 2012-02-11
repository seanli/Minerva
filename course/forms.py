from django import forms
from django.forms import ModelChoiceField
from Minerva.core.forms import DivErrorList, StandardForm
from Minerva.core.models import Institute, Course, Profile, Section, SectionAssign
from Minerva.core.utilities import titlecase
import datetime

class AddCourseForm(StandardForm):
    
    class InstructorChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return obj.user.get_full_name()
    
    name = forms.CharField(max_length=100, label='Course Name')
    first_day = forms.DateField(label='First Day', initial=datetime.datetime.today().strftime('%m/%d/%Y'), widget=forms.DateInput(attrs={'data-datepicker':'datepicker'}))
    last_day = forms.DateField(label='Last Day', initial=datetime.datetime.today().strftime('%m/%d/%Y'), widget=forms.DateInput(attrs={'data-datepicker':'datepicker'}))
    instructor = InstructorChoiceField(label='Instructor', queryset=None)
    
    def __init__(self, *args, **kwargs):
        try:
            source = kwargs.pop('source')
        except:
            source = "[]"
        super(AddCourseForm, self).__init__(*args, **kwargs)
        self.profile = self.request.user.get_profile()
        self.fields["name"].widget = forms.TextInput(attrs={'data-provide':'typeahead', 'data-items':'7', 'autocomplete':'off', 'data-source':source})
        self.fields["instructor"].queryset = Profile.objects.filter(role='I', institute=self.profile.institute)
        
    def clean_name(self):
        name = titlecase(self.cleaned_data["name"].strip())
        return name
    
    def clean(self):
        data = self.cleaned_data
        if self._errors:
            return data
        else:
            institute = self.profile.institute
            if Course.objects.filter(name__icontains=data['name'], institute=institute).count() == 0:
                raise forms.ValidationError('<strong>%s</strong> for <strong>%s</strong> is not a registered course!' % (data['name'], institute))
            else:
                data['course'] = Course.objects.filter(name__icontains=data['name'], institute=institute)[0]
                try:
                    section = Section.objects.get(course=data['course'], first_day=data['first_day'], last_day=data['last_day'], instructor=data['instructor'])
                    data['section'] = section
                except Section.DoesNotExist:
                    section = None
                if section != None and SectionAssign.objects.filter(section=section, profile=self.profile).count() > 0:
                    raise forms.ValidationError('You are already registered in this course section!')
                return data