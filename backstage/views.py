from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from backstage.models import Ticket, Wiki
from backstage.forms import TicketForm
from core.decorators import staff_required
from creoleparser import text2html


@login_required
@staff_required
def dashboard(request):
    context = RequestContext(request)
    return render_to_response('backstage/dashboard.html', context)


@login_required
@staff_required
def tickets(request, ticket_id=None):
    context = RequestContext(request)
    if ticket_id is None:
        ticket_list = Ticket.objects.all()
        context['tickets'] = ticket_list
        return render_to_response('backstage/tickets.html', context)
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
            context['ticket'] = ticket
            context['form'] = form
            return render_to_response('backstage/tickets_detail.html', context)
        else:
            return HttpResponse('Ticket Not Found!')


@login_required
@staff_required
def wiki(request, wiki_id=None):
    context = RequestContext(request)
    if wiki_id is None:
        wiki_list = Wiki.objects.all()
        context['wikis'] = wiki_list
        return render_to_response('backstage/wiki.html', context)
    else:
        try:
            wiki = Wiki.objects.get(id=wiki_id)
        except Wiki.DoesNotExist:
            wiki = None
        if wiki is not None:
            context['wiki'] = wiki
            context['parsed'] = text2html(wiki.document)
            return render_to_response('backstage/wiki_detail.html', context)
        else:
            return HttpResponse('Wiki Not Found!')
