from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


@login_required
def homeroom(request):
    context = RequestContext(request)
    return render_to_response('homeroom/main.html', context)
