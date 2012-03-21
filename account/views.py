from django.contrib import auth
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from account.forms import LoginForm, SignupForm
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
    return render_to_response('account/login.html',
        {'form': form, 'referrer': referrer}, context_instance=RequestContext(request))


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
    return render_to_response('account/signup.html',
        {'form': form}, context_instance=RequestContext(request))
