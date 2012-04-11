from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from course.models import Course
from core.models import Specialization, Skill
from django.utils import simplejson
from django.db.models import Q


@login_required
def autocomplete_course(request):
    json = []
    if 'term' in request.GET:
        term = request.GET['term']
        courses = Course.objects.filter(Q(title__icontains=term) | Q(abbrev__icontains=term)).order_by('title')[:7]
        for course in courses:
            datum = {}
            datum['title'] = course.title
            datum['abbrev'] = course.abbrev
            datum['value'] = course.id
            json.append(datum)
    return HttpResponse(simplejson.dumps(json))


@login_required
def autocomplete_specialization(request):
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
def autocomplete_skill(request):
    json = []
    if 'term' in request.GET:
        term = request.GET['term']
        skills = Skill.objects.filter(name__istartswith=term).order_by('name')[:10]
        for skill in skills:
            datum = {}
            datum['label'] = skill.name
            datum['value'] = skill.id
            json.append(datum)
    return HttpResponse(simplejson.dumps(json))
