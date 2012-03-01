from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from Minerva.backstage.models import Ticket


@login_required
def home(request):
    tickets = Ticket.objects.all()
    context = {
        'tickets': tickets,
    }
    return render_to_response('backstage/home.html', context, context_instance=RequestContext(request))
