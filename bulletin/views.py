from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext


@login_required
def bulletin(request):
    #results = SearchQuerySet().autocomplete(text='software').models(Course)
    #suggestion = SearchQuerySet().spelling_suggestion('algorithasm')
    #print suggestion
    context = RequestContext(request)
    return render_to_response('bulletin/main.html', context)
