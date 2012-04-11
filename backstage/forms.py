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


class WikiForm(StandardForm):

    title = forms.CharField(label='Title')
    document = forms.CharField(label='Document', widget=forms.Textarea(attrs={'style': 'width:98%;resize:vertical'}))

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        return title

    def clean_document(self):
        document = self.cleaned_data['document'].strip()
        return document
