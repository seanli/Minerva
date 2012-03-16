from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from creoleparser import text2html

@login_required
def homeroom(request):
    context = RequestContext(request)
    context['display'] = text2html("|=|=table|=header|\n|a|table|row|\n|b|table|row|")
    return render_to_response('homeroom/main.html', context)
