from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from Minerva.account.forms import ReportForm
from Minerva.core.models import Report
from Minerva.core.ajax import clear_validation, show_validation

@dajaxice_register
def form_report(request, form_data, form_id):
    try:
        dajax = Dajax()
        form = ReportForm(form_data)
        if form.is_valid():
            clear_validation(dajax, form, form_id)
            data = form.cleaned_data
            message = data['message']
            report = Report()
            report.message = message
            if request.user.is_authenticated():
                report.reporter = request.user.get_profile()
            else:
                report.reporter = None
            report.save()
            dajax.add_data({'status': 'OK'}, 'form_report_callback')
        else:
            clear_validation(dajax, form, form_id)
            show_validation(dajax, form, form_id)
        return dajax.json()
    except Exception, e:
        print e
