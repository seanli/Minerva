from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.contrib.auth.decorators import login_required
from portfolio.forms import EncouragementForm, AddSpecializationForm, AddSkillForm
from core.models import Encouragement, SkillAssign
from core.ajax import clear_validation, show_validation
from datetime import datetime
from django.utils import simplejson


@dajaxice_register
@login_required
def form_encouragement(request, form_data):
    dajax = Dajax()
    form = EncouragementForm(form_data, request=request)
    if form.is_valid():
        clear_validation(dajax, form)
        data = form.cleaned_data
        message = data['message']
        person_to = data['person_to']
        anonymous = data['anonymous']
        if person_to != request.user:
            encouragement = Encouragement()
            encouragement.message = message
            encouragement.person_to = person_to
            encouragement.person_from = request.user
            encouragement.anonymous = anonymous
            encouragement.sent_time = datetime.now()
            encouragement.save()
            dajax.add_data({'status': 'OK'}, 'form_encouragement_callback')
        else:
            clear_validation(dajax, form)
            show_validation(dajax, form)
            dajax.add_data({'status': 'INVALID'}, 'form_encouragement_callback')
    else:
        clear_validation(dajax, form)
        show_validation(dajax, form)
        dajax.add_data({'status': 'INVALID'}, 'form_encouragement_callback')
    return dajax.json()


@dajaxice_register
@login_required
def form_add_specialization(request, form_data):
    dajax = Dajax()
    form = AddSpecializationForm(form_data, request=request)
    if form.is_valid():
        clear_validation(dajax, form)
        data = form.cleaned_data
        specialization = data['specialization']
        user = request.user
        user.add_specialization(specialization)
        dajax.add_data({'status': 'OK'}, 'form_add_specialization_callback')
    else:
        clear_validation(dajax, form)
        show_validation(dajax, form)
        dajax.add_data({'status': 'INVALID'}, 'form_add_specialization_callback')
    return dajax.json()


@dajaxice_register
@login_required
def form_add_skill(request, form_data):
    dajax = Dajax()
    form = AddSkillForm(form_data, request=request)
    if form.is_valid():
        clear_validation(dajax, form)
        data = form.cleaned_data
        skill = data['skill']
        user = request.user
        user.add_skill(skill)
        dajax.add_data({'status': 'OK'}, 'form_add_skill_callback')
    else:
        clear_validation(dajax, form)
        show_validation(dajax, form)
        dajax.add_data({'status': 'INVALID'}, 'form_add_skill_callback')
    return dajax.json()


@dajaxice_register
@login_required
def approve_encouragement(request, encouragement_id, approve):
    status = 'OK'
    try:
        encouragement = Encouragement.objects.get(pk=encouragement_id)
        # Ensure a user is approving his/her own encouragements
        if encouragement.person_to != request.user:
            status = 'INVALID'
    except Encouragement.DoesNotExist:
        status = 'INVALID'
    encouragement.approve(approve)
    return simplejson.dumps({'status': status})


@dajaxice_register
@login_required
def rate_skill(request, skill_assign_id, rating):
    status = 'OK'
    user = request.user
    try:
        skill_assign = SkillAssign.objects.get(id=skill_assign_id)
        user.rate_skill(skill_assign, rating)
    except SkillAssign.DoesNotExist:
        status = 'INVALID'
    return simplejson.dumps({'status': status})


@dajaxice_register
@login_required
def plus_exp(request):
    profile = request.user.get_profile()
    profile.increment_grade(20)
    return simplejson.dumps({
        'grade': profile.get_grade_display(),
        'exp': profile.grade_gauge,
    })


@dajaxice_register
@login_required
def minus_exp(request):
    profile = request.user.get_profile()
    profile.increment_grade(-20)
    return simplejson.dumps({
        'grade': profile.get_grade_display(),
        'exp': profile.grade_gauge,
    })
