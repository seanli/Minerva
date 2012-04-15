from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from core.forms import StandardForm, GenericField, LegendWidget
from core.utilities import titlecase
from core.models import Institute
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

    personal_detail = GenericField(widget=LegendWidget(attrs={'display': 'Personal Detail'}))
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    institute = forms.ModelChoiceField(queryset=Institute.objects, empty_label=None, label='Institute')
    role = forms.ChoiceField(choices=ROLE, label='Who are you?')
    login_credential = GenericField(widget=LegendWidget(attrs={'display': 'Login Credential'}))
    email = forms.EmailField(max_length=75, label='Email')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Password')
    password_conf = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Confirm Password')

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


class SettingForm(StandardForm):
    password_old = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Old Password')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Password')
    password_conf = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Confirm Password')

    def clean_password_old(self):
        if not self.request.user.check_password(self.cleaned_data['password_old']):
            raise forms.ValidationError('Incorrect password!')

    def clean_password_conf(self):
        password = self.cleaned_data['password']
        password_conf = self.cleaned_data['password_conf']
        if password != password_conf:
            raise forms.ValidationError('Passwords do not match!')
        return password
