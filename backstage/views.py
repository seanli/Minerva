from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from backstage.models import Ticket
from core.decorators import staff_required


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


@login_required
@staff_required
def cms(request):
    admin_frame_location = request.COOKIES.get('admin_frame_location', None)
    # Process iframe URL
    if admin_frame_location is not None:
        split_location = str(admin_frame_location).replace("%2F", "/").replace("%3F", "?").replace("%3D", "=").split('/')
        new_location = '/' + ('/').join(split_location[3:])
        if '%' in new_location:
            new_location = '/admin'
    else:
        new_location = '/admin'
    context = {
        'admin_frame_location': new_location,
    }
    return render_to_response('backstage/cms.html', context, context_instance=RequestContext(request))
