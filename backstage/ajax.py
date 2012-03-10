from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from backstage.forms import ReportForm
from backstage.models import Ticket
from core.ajax import clear_validation, show_validation


@dajaxice_register
def form_report(request, form_data, form_id):
    dajax = Dajax()
    form = ReportForm(form_data)
    if form.is_valid():
        clear_validation(dajax, form, form_id)
        data = form.cleaned_data
        message = data['message']
        report = Ticket()
        report.summary = message[:100]
        report.description = message
        if request.user.is_authenticated():
            report.reporter = request.user
        report.save()
        dajax.add_data({'status': 'OK'}, 'form_report_callback')
    else:
        clear_validation(dajax, form, form_id)
        show_validation(dajax, form, form_id)
        dajax.add_data({'status': 'INVALID'}, 'form_report_callback')
    return dajax.json()
