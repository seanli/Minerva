from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext


def error_403(request):
    return render_to_response('403.html', RequestContext(request))


def error_404(request):
    return render_to_response('404.html', RequestContext(request))


def error_500(request):
    return render_to_response('500.html', RequestContext(request))


@login_required
def bulletin(request):
    return render_to_response('bulletin.html', RequestContext(request))
