from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from account.forms import LoginForm, SignupForm, AddSpecializationForm, AddSkillForm
from account.models import Profile
from core.models import BadgeAssign, Encouragement, Specialization, Skill
from core.utilities import get_referrer, set_referrer
from django.utils import simplejson


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


@login_required
def crowd(request, username=None):
    if username == None:
        user = request.user
    else:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
    if user is not None:
        profile = user.get_profile()

        add_specialization_form = AddSpecializationForm(request=request)
        add_skill_form = AddSkillForm(request=request)

        context = {
            'viewing_user': user,
            'profile': profile,
            'badges': BadgeAssign.objects.filter(user=user),
            'encouragements': Encouragement.objects.filter(person_to=user).order_by('-sent_time'),
            'related': Profile.objects.filter(institute=profile.institute, role='S').exclude(id=request.user.profile.id).exclude(id=profile.id),
            'add_specialization_form': add_specialization_form,
            'add_skill_form': add_skill_form
        }
        return render_to_response('crowd/main.html', context, context_instance=RequestContext(request))
    else:
        return HttpResponse('User Not Found!')


@login_required
def source_specialization(request):
    json = []
    if 'term' in request.GET:
        term = request.GET['term']
        specializations = Specialization.objects.filter(name__icontains=term).order_by('name')[:7]
        for specialization in specializations:
            datum = {}
            datum['label'] = specialization.name
            datum['value'] = specialization.id
            json.append(datum)
    return HttpResponse(simplejson.dumps(json))


@login_required
def source_skill(request):
    json = []
    if 'term' in request.GET:
        term = request.GET['term']
        skills = Skill.objects.filter(name__icontains=term).order_by('name')[:7]
        for skill in skills:
            datum = {}
            datum['label'] = skill.name
            datum['value'] = skill.id
            json.append(datum)
    return HttpResponse(simplejson.dumps(json))
