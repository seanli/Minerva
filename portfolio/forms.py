from django import forms
from django.contrib.auth.models import User
from core.forms import StandardForm
from core.models import Specialization, Skill


class EncouragementForm(StandardForm):

    message = forms.CharField(label='Please Write Your Encouragement Below...', widget=forms.Textarea(attrs={'style': 'width:98%;resize:vertical'}))
    anonymous = forms.BooleanField(label='Anonymous?', required=False, initial=False)
    person_to = forms.ModelChoiceField(label='', queryset=User.objects, widget=forms.HiddenInput())

    def clean_message(self):
        message = self.cleaned_data['message'].strip()
        return message


class AddSpecializationForm(StandardForm):

    name = forms.CharField(max_length=100, label='Specialization', widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    specialization = forms.ModelChoiceField(label='', queryset=Specialization.objects, widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(AddSpecializationForm, self).__init__(*args, **kwargs)
        self.user = self.request.user

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        return name

    def clean(self):
        data = self.cleaned_data
        if self._errors:
            return data
        else:
            specialization = data['specialization']
            if specialization is None:
                raise forms.ValidationError('<strong>%s</strong> is not a listed specialization!' % data['name'])
            else:
                if self.user.has_specialization(specialization):
                    raise forms.ValidationError('You have already added this specialization!')
                return data


class AddSkillForm(StandardForm):

    name = forms.CharField(max_length=100, label='Skill', widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    skill = forms.ModelChoiceField(label='', queryset=Skill.objects, widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(AddSkillForm, self).__init__(*args, **kwargs)
        self.user = self.request.user

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        return name

    def clean(self):
        data = self.cleaned_data
        if self._errors:
            return data
        else:
            skill = data['skill']
            if skill is None:
                raise forms.ValidationError('<strong>%s</strong> is not a listed skill!' % data['name'])
            else:
                if self.user.has_skill(skill):
                    raise forms.ValidationError('You have already added this skill!')
                return data
