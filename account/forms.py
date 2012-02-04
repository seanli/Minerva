from django import forms
from django.contrib import auth
from core.forms import DivErrorList

class LoginForm(forms.Form):
    
    emailname = forms.CharField(max_length=100, label='Email/Username', error_messages={'required': 'Please put your email/username!'})
    password = forms.CharField(widget=forms.PasswordInput, label='Password', error_messages={'required': 'Please put your password!'})
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.error_class = DivErrorList
        
    def clean(self):
        data = self.cleaned_data
        username = data.get('emailname', None)
        password = data.get('password', None)
        if username is not None and password is not None:
            user = auth.authenticate(username=username, password=password)
            if user is None or not user.is_active:
                raise forms.ValidationError('Username/email or password is invalid!')
            else:
                data['user'] = user
            return data

            