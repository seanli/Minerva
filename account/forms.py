from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from core.forms import StandardForm
from core.utilities import titlecase
from core.models import Institute, Specialization, Skill
from core.constants import ROLE


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
            if user is None:
                raise forms.ValidationError('Email or password is invalid!')
            elif not user.is_active:
                raise forms.ValidationError('Account needs to be activated!')
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
        self.profile = self.request.user.get_profile()

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
                if self.profile.has_specialization(specialization):
                    raise forms.ValidationError('You have already added this specialization!')
                return data


class AddSkillForm(StandardForm):

    name = forms.CharField(max_length=100, label='Skill', widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    skill = forms.ModelChoiceField(label='', queryset=Skill.objects, widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(AddSkillForm, self).__init__(*args, **kwargs)
        self.profile = self.request.user.get_profile()

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
                if self.profile.has_skill(skill):
                    raise forms.ValidationError('You have already added this skill!')
                return data
