from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from Minerva.account.forms import LoginForm, SignupForm
from Minerva.core.models import Profile
from Minerva.core.utilities import unique_username, get_referrer, set_referrer

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = data['user']
            auth.login(request, user)
            return HttpResponseRedirect(reverse('bulletin'))
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
            user = User()
            user.username = unique_username(data['first_name'], data['last_name'])
            user.email = data['email']
            user.set_password(data['password'])
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()
            profile = Profile()
            profile.user = user
            profile.institute = data['institute']
            profile.role = data['role']
            profile.save()
            set_referrer(request, 'signup')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = SignupForm()
    return render_to_response('account/signup.html',
        {'form': form}, context_instance=RequestContext(request))
    
def people(request, username):
    data = {
        'username': username,
    }
    return render_to_response('account/people.html', data, context_instance=RequestContext(request))