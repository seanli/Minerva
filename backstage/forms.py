from django import forms
from core.forms import StandardForm, StandardModelForm
from backstage.models import Ticket


class ReportForm(StandardForm):

    message = forms.CharField(label='Please Write Your Report Below...', widget=forms.Textarea(attrs={'style': 'width:98%;resize:vertical'}))

    def clean_message(self):
        message = self.cleaned_data['message'].strip()
        return message


class TicketForm(StandardModelForm):

    class Meta:
        model = Ticket
