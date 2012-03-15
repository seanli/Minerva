from django import forms
from django.forms import ModelChoiceField
from core.forms import StandardForm
from django.contrib.auth.models import User
from course.models import Course, Section
from datetime import datetime, timedelta


class AddCourseForm(StandardForm):

    class InstructorChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return obj.get_full_name()

    title = forms.CharField(max_length=100, label='Course Title')
    first_day = forms.DateField(label='First Day', initial=datetime.today().strftime('%m/%d/%Y'), widget=forms.DateInput(attrs={'data-datepicker': 'datepicker'}))
    last_day = forms.DateField(label='Last Day', initial=(datetime.today() + timedelta(days=1)).strftime('%m/%d/%Y'), widget=forms.DateInput(attrs={'data-datepicker': 'datepicker'}))
    instructor = InstructorChoiceField(label='Instructor', queryset=None)

    def __init__(self, *args, **kwargs):
        try:
            source = kwargs.pop('source')
        except:
            source = "[]"
        super(AddCourseForm, self).__init__(*args, **kwargs)
        self.profile = self.request.user.get_profile()
        self.fields["title"].widget = forms.TextInput(attrs={'data-provide': 'typeahead', 'data-items': '7', 'autocomplete': 'off', 'data-source': source})
        self.fields["instructor"].queryset = User.objects.filter(profile__role='I', profile__institute=self.profile.institute)

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        return title

    def clean_last_day(self):
        first_day = self.cleaned_data['first_day']
        last_day = self.cleaned_data['last_day']
        if last_day <= first_day:
            raise forms.ValidationError('Invalid date range')
        return last_day

    def clean(self):
        data = self.cleaned_data
        if self._errors:
            return data
        else:
            institute = self.profile.institute
            course = Course.get(title=data['title'], institute=institute)
            if course is None:
                raise forms.ValidationError('<strong>%s</strong> for <strong>%s</strong> is not a registered course!' % (data['title'], institute))
            else:
                data['course'] = course
                try:
                    section = Section.objects.get(course=data['course'], first_day=data['first_day'], last_day=data['last_day'], instructor=data['instructor'])
                    data['section'] = section
                except Section.DoesNotExist:
                    section = None
                if section != None and self.profile.has_section(section):
                    raise forms.ValidationError('You are already registered in this course section!')
                return data
