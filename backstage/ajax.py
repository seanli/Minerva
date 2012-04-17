from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from backstage.forms import ReportForm
from backstage.models import Ticket
from core.ajax import clear_validation, show_validation


@dajaxice_register
def form_report(request, form_data):
    dajax = Dajax()
    callback = 'form_report_callback'
    form = ReportForm(form_data)
    if form.is_valid():
        clear_validation(dajax, form)
        data = form.cleaned_data
        message = data['message']
        report = Ticket()
        report.summary = message[:100]
        report.description = message
        if request.user.is_authenticated():
            report.reporter = request.user
        report.save()
        dajax.add_data({'status': 'OK'}, callback)
    else:
        show_validation(dajax, form)
        dajax.add_data({'status': 'INVALID'}, callback)
    return dajax.json()
