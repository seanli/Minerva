from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from Minerva.core.models import BadgeAssign

@login_required
def home(request):
    profile = request.user.get_profile()
    badges = BadgeAssign.objects.filter(profile=profile)
    return render_to_response('home.html', {'badges': badges}, context_instance=RequestContext(request))