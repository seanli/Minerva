from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from core.algorithms import string_similarity
from course.models import Course


@login_required
def bulletin(request):
    course_titles = [course.title for course in Course.objects.all()]
    similarities = []
    match_text = 'sotfwaer engieenring'
    for title in course_titles:
        similarity = string_similarity(match_text, title, boost=True)
        if similarity > 0.5:
            datum = {}
            datum['title'] = title
            datum['similarity'] = similarity
            similarities.append(datum)
    context = RequestContext(request)
    context['similarities'] = sorted(similarities, key=lambda s: s['similarity'], reverse=True)
    return render_to_response('bulletin/main.html', context)
