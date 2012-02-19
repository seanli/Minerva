from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from Minerva.account.forms import LoginForm, SignupForm, AddSpecializationForm, AddSkillForm
from Minerva.core.models import Profile, BadgeAssign, Encouragement, Specialization, Skill
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

@login_required
def people(request, username=None):
    if username == None:
        user = request.user
    else:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
    if user is not None:
        profile = user.get_profile()
        
        source = ''
        specializations = Specialization.objects.all()
        last = len(specializations) - 1
        index = 0
        for specialization in specializations:
            if (index != last):
                source += '"%s",' % (specialization.name)
            else:
                source += '"%s"' % (specialization.name)
            index += 1
        source = '[' + source + ']'
        add_specialization_form = AddSpecializationForm(request=request, source=source)
        
        source = ''
        skills = Skill.objects.all()
        last = len(skills) - 1
        index = 0
        for skill in skills:
            if (index != last):
                source += '"%s",' % (skill.name)
            else:
                source += '"%s"' % (skill.name)
            index += 1
        source = '[' + source + ']'
        add_skill_form = AddSkillForm(request=request, source=source)
        
        context = {
            'current_user': user,
            'profile': profile,
            'badges': BadgeAssign.objects.filter(profile=profile),
            'encouragements': Encouragement.objects.filter(person_to=profile).order_by('-sent_time'),
            'related': Profile.objects.filter(institute=profile.institute, role='S').exclude(id=request.user.profile.id).exclude(id=profile.id),
            'add_specialization_form': add_specialization_form,
            'add_skill_form': add_skill_form
        }
        return render_to_response('account/people.html', context, context_instance=RequestContext(request))
    else:
        return HttpResponse('User Not Found!')
