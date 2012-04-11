from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import RequestContext
from backstage.models import (Ticket, Wiki, WikiRevisionHistory,
    LogMessage)
from backstage.forms import TicketForm, WikiForm
from core.decorators import staff_required
from creoleparser import text2html
from datetime import datetime
import logging


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
def tickets_create(request, ticket_id=None):
    context = RequestContext(request)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('backstage/ticket_create_success.html', context)
    else:
        form = TicketForm()
    context['form'] = form
    return render_to_response('backstage/tickets_create.html', context)


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
            wiki_obj = Wiki.objects.get(id=wiki_id)
        except Wiki.DoesNotExist:
            wiki_obj = None
        if wiki_obj is not None:
            context['wiki'] = wiki_obj
            context['parsed'] = text2html(wiki_obj.document)
            context['revisions'] = WikiRevisionHistory.objects.filter(wiki=wiki_obj).order_by('-created_time')
            return render_to_response('backstage/wiki_detail.html', context)
        else:
            return HttpResponse('Wiki Not Found!')


@login_required
@staff_required
def wiki_edit(request, wiki_id=None):
    context = RequestContext(request)
    if request.method == 'POST':
        form = WikiForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = request.user
            try:
                wiki_obj = Wiki.objects.get(id=wiki_id)
            except Wiki.DoesNotExist:
                wiki_obj = Wiki()
                wiki_obj.author = user
            wiki_obj.title = data['title']
            wiki_obj.document = data['document']
            wiki_obj.save(user=user)
            return redirect('/backstage/wiki/%s' % wiki_obj.id)
    else:
        edit = False
        try:
            wiki_obj = Wiki.objects.get(id=wiki_id)
            form = WikiForm({'title': wiki_obj.title, 'document': wiki_obj.document})
            edit = True
        except Wiki.DoesNotExist:
            form = WikiForm()
        context['edit'] = edit
    context['form'] = form
    return render_to_response('backstage/wiki_edit.html', context)


@csrf_exempt
def onerror(request):
    if request.method != 'POST':
        ret = HttpResponse(content='POST Only', status=400)
    else:
        message = request.POST['message']
        line_number = request.POST['line_number']
        url = request.POST['url']
        log_message = LogMessage()
        log_message.logged_time = datetime.now()
        log_message.logger_name = 'client'
        log_message.level = logging.ERROR
        log_message.line_number = line_number
        log_message.message = message
        log_message.uri_path = url
        log_message.request = request
        if request.user.is_authenticated():
            log_message.user = request.user
        log_message.save()
        ret = HttpResponse(content='Success', status=201)
    return ret
