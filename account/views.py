from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from account.forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = data['user']
            auth.login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = LoginForm()
    return render_to_response('account/login.html',
        {'form': form}, context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))