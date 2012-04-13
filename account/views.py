from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from account.forms import LoginForm, SignupForm, SettingForm
from account.models import Profile
from core.utilities import get_referrer, set_referrer


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = data['user']
            auth.login(request, user)
            redirect_to = request.REQUEST.get('next', reverse('home'))
            return HttpResponseRedirect(redirect_to)
    else:
        form = LoginForm()
    referrer = get_referrer(request)
    context = RequestContext(request)
    context['form'] = form
    context['referrer'] = referrer
    return render_to_response('account/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Profile.register_user(email=data['email'], password=data['password'], first_name=data['first_name'],
                last_name=data['last_name'], institute=data['institute'], role=data['role'])
            set_referrer(request, 'signup')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = SignupForm()
    context = RequestContext(request)
    context['form'] = form
    return render_to_response('account/signup.html', context)
def setting(request):
    if request.method == 'POST':
        form = SettingForm(request.POST,request=request)
        if form.is_valid():
            data = form.cleaned_data
            form.set_password()
    else:
        form = SettingForm()
    context = RequestContext(request)
    context['form'] = form
    return render_to_response('account/setting.html', context)
