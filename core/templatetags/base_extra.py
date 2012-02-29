from django import template
from datetime import datetime
from django.conf import settings
from Minerva.account.forms import ReportForm, EncouragementForm


register = template.Library()


@register.simple_tag
def brand_name():
    return settings.BRAND_NAME


@register.simple_tag
def active(request, sub_url):
    if sub_url in request.path or (sub_url == 'bulletin' and request.path == '/'):
        return "active"
    return ""


@register.simple_tag
def current_year():
    return unicode(datetime.now().year)


@register.tag
def report_form(parser, token):
    return ReportFormNode()


class ReportFormNode(template.Node):
    def render(self, context):
        context['report_form'] = ReportForm()
        return ''


@register.tag
def encouragement_form(parser, token):
    return EncouragementFormNode()


class EncouragementFormNode(template.Node):
    def render(self, context):
        context['encouragement_form'] = EncouragementForm()
        return ''
