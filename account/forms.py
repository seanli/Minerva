from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from Minerva.core.forms import StandardForm
from Minerva.core.utilities import titlecase
from Minerva.core.models import (Institute, Specialization, Skill)
from Minerva.core.references import ROLE


class LoginForm(StandardForm):

    emailname = forms.CharField(max_length=75, label='Email', error_messages={'required': 'Please put your email!'})
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Password', error_messages={'required': 'Please put your password!'})

    def clean(self):
        data = self.cleaned_data
        if self._errors:
            return data
        else:
            username = data['emailname'].strip()
            password = data['password']
            user = auth.authenticate(username=username, password=password)
            if user is None or not user.is_active:
                raise forms.ValidationError('Email or password is invalid!')
            else:
                data['user'] = user
            return data


class SignupForm(StandardForm):

    email = forms.EmailField(max_length=75, label='Email')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Password')
    password_conf = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Confirm Password')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    institute = forms.ModelChoiceField(queryset=Institute.objects, empty_label=None, label='Institute')
    role = forms.ChoiceField(choices=ROLE, label='Who are you?')

    def clean_email(self):
        email = self.cleaned_data['email'].lower().strip()
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already taken!')

    def clean_password_conf(self):
        password = self.cleaned_data['password']
        password_conf = self.cleaned_data['password_conf']
        if password != password_conf:
            raise forms.ValidationError('Passwords do not match!')
        return password

    def clean_first_name(self):
        first_name = titlecase(self.cleaned_data['first_name'].strip())
        return first_name

    def clean_last_name(self):
        last_name = titlecase(self.cleaned_data['last_name'].strip())
        return last_name


class ReportForm(StandardForm):

    message = forms.CharField(label='Please Write Your Report Below...', widget=forms.Textarea(attrs={'style':'width:98%;resize:vertical'}))

    def clean_message(self):
        message = self.cleaned_data['message'].strip()
        return message


class EncouragementForm(StandardForm):

    message = forms.CharField(label='Please Write Your Encouragement Below...', widget=forms.Textarea(attrs={'style':'width:98%;resize:vertical'}))
    anonymous = forms.BooleanField(label='Anonymous?', required=False, initial=False)
    person_to = forms.ModelChoiceField(label='', queryset=User.objects, widget=forms.HiddenInput())

    def clean_message(self):
        message = self.cleaned_data['message'].strip()
        return message


class AddSpecializationForm(StandardForm):

    name = forms.CharField(max_length=100, label='Specialization')

    def __init__(self, *args, **kwargs):
        try:
            source = kwargs.pop('source')
        except:
            source = "[]"
        super(AddSpecializationForm, self).__init__(*args, **kwargs)
        self.profile = self.request.user.get_profile()
        self.fields["name"].widget = forms.TextInput(attrs={'data-provide':'typeahead', 'data-items':'7', 'autocomplete':'off', 'data-source':source})

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        return name

    def clean(self):
        data = self.cleaned_data
        if self._errors:
            return data
        else:
            specialization = Specialization.get(data['name'])
            if specialization is None:
                raise forms.ValidationError('<strong>%s</strong> is not a listed specialization!' % data['name'])
            else:
                if self.profile.has_specialization(specialization):
                    raise forms.ValidationError('You have already added this specialization!')
                else:
                    data['specialization'] = specialization
                return data


class AddSkillForm(StandardForm):

    name = forms.CharField(max_length=100, label='Skill')

    def __init__(self, *args, **kwargs):
        try:
            source = kwargs.pop('source')
        except:
            source = "[]"
        super(AddSkillForm, self).__init__(*args, **kwargs)
        self.profile = self.request.user.get_profile()
        self.fields['name'].widget = forms.TextInput(attrs={'data-provide':'typeahead', 'data-items':'7', 'autocomplete':'off', 'data-source':source})

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        return name

    def clean(self):
        data = self.cleaned_data
        if self._errors:
            return data
        else:
            skill = Skill.get(data['name'])
            if skill is None:
                raise forms.ValidationError('<strong>%s</strong> is not a listed skill!' % data['name'])
            else:
                if self.profile.has_skill(skill):
                    raise forms.ValidationError('You have already added this skill!')
                else:
                    data['skill'] = skill
                return data
