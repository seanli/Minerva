from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from core.forms import DivErrorList
from core.utilities import titlecase
from core.models import Institute
from core.references import ROLE

class LoginForm(forms.Form):
    
    emailname = forms.CharField(max_length=75, label='Email', error_messages={'required': 'Please put your email!'})
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Password', error_messages={'required': 'Please put your password!'})
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList
    
    def clean(self):
        data = self.cleaned_data
        username = data.get('emailname', '').strip()
        password = data.get('password', '')
        if username is not '' and password is not '':
            user = auth.authenticate(username=username, password=password)
            if user is None or not user.is_active:
                raise forms.ValidationError('Email or password is invalid!')
            else:
                data['user'] = user
            return data

class SignupForm(forms.Form):
    
    email = forms.EmailField(max_length=75, label='Email')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Password')
    password_conf = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Confirm Password')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    institute = forms.ModelChoiceField(queryset=Institute.objects, empty_label=None, label='Institute')
    role = forms.ChoiceField(choices=ROLE, label='Who are you?')
    
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList
        
    def clean_email(self):
        email = self.cleaned_data["email"].lower().strip()
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email address is already taken!')

    def clean_password_conf(self):
        password = self.cleaned_data["password"]
        password_conf = self.cleaned_data["password_conf"]
        if password != password_conf:
            raise forms.ValidationError('Passwords do not match!')
        return password
    
    def clean_first_name(self):
        first_name = titlecase(self.cleaned_data["first_name"].strip())
        return first_name
    
    def clean_last_name(self):
        last_name = titlecase(self.cleaned_data["last_name"].strip())
        return last_name
    