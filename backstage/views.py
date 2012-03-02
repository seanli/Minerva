from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from Minerva.backstage.models import Ticket
from Minerva.core.decorators import staff_required


@login_required
@staff_required
def dashboard(request):
    return render_to_response('backstage/dashboard.html', context_instance=RequestContext(request))


@login_required
@staff_required
def tickets(request):
    tickets = Ticket.objects.all()
    context = {
        'tickets': tickets,
    }
    return render_to_response('backstage/tickets.html', context, context_instance=RequestContext(request))
