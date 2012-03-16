from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from backstage.models import Ticket
from backstage.forms import TicketForm
from core.decorators import staff_required


@login_required
@staff_required
def dashboard(request):
    return render_to_response('backstage/dashboard.html', context_instance=RequestContext(request))


@login_required
@staff_required
def tickets(request, ticket_id=None):
    if ticket_id is None:
        ticket_list = Ticket.objects.all()
        context = {
            'tickets': ticket_list,
        }
        return render_to_response('backstage/tickets.html', context, context_instance=RequestContext(request))
    else:
        try:
            ticket = Ticket.objects.get(id=ticket_id)
        except Ticket.DoesNotExist:
            ticket = None
        if ticket is not None:
            if request.method == 'POST':
                form = TicketForm(request.POST, instance=ticket)
                if form.is_valid():
                    form.save()
            else:
                form = TicketForm(instance=ticket)
            context = {
                'ticket': ticket,
                'form': form,
            }
            return render_to_response('backstage/tickets_detail.html', context, context_instance=RequestContext(request))
        else:
            return HttpResponse('Ticket Not Found!')
