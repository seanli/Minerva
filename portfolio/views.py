from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from portfolio.forms import AddSpecializationForm, AddSkillForm, EncouragementForm
from account.models import Profile
from core.models import BadgeAssign, Encouragement, SkillAssign, SkillRating


@login_required
def portfolio(request, username=None):
    user = request.user
    if username == None:
        viewing_user = user
    else:
        try:
            viewing_user = User.objects.get(username=username)
        except User.DoesNotExist:
            viewing_user = None
    if viewing_user is not None:
        profile = viewing_user.get_profile()
        user_skills = SkillAssign.objects.filter(user=viewing_user)
        skills_data = []
        for user_skill in user_skills:
            skill_data = {}
            skill_data['id'] = user_skill.id
            skill_data['skill'] = user_skill.skill
            rating_sum = sum([rating.value for rating in user_skill.skillrating_set.all()])
            total_ratings = user_skill.skillrating_set.filter(value__gt=0).count()
            if total_ratings > 0:
                skill_data['average_rating'] = round(rating_sum / float(total_ratings), 2)
            else:
                skill_data['average_rating'] = 0
            skill_data['total_ratings'] = total_ratings
            try:
                skill_rating = SkillRating.objects.get(rater=user, skill_assign=user_skill).value
            except SkillRating.DoesNotExist:
                skill_rating = 0
            skill_data['skill_rating'] = skill_rating
            skills_data.append(skill_data)

        add_specialization_form = AddSpecializationForm(request=request)
        add_skill_form = AddSkillForm(request=request)
        encouragement_form = EncouragementForm(request=request)

        context = RequestContext(request)
        context['viewing_user'] = viewing_user
        context['profile'] = profile
        context['skills_data'] = skills_data
        context['badges'] = BadgeAssign.objects.filter(user=viewing_user)
        context['encouragements_unapproved'] = Encouragement.objects.filter(person_to=viewing_user, approved=False).order_by('-sent_time')
        context['encouragements_approved'] = Encouragement.objects.filter(person_to=viewing_user, approved=True).order_by('-sent_time')
        context['related'] = Profile.objects.filter(institute=profile.institute, role='S').exclude(id=request.user.profile.id).exclude(id=profile.id)
        context['add_specialization_form'] = add_specialization_form
        context['add_skill_form'] = add_skill_form
        context['encouragement_form'] = encouragement_form
        return render_to_response('portfolio/main.html', context)
    else:
        return HttpResponse('User Not Found!')
