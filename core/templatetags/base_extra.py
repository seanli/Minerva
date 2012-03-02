from django import template
from datetime import datetime
from django.conf import settings
from Minerva.account.forms import EncouragementForm
from Minerva.backstage.forms import ReportForm


register = template.Library()


@register.simple_tag
def brand_name():
    return settings.BRAND_NAME


@register.simple_tag
def active(request, sub_urls):
    # Sub-URLs are joined by '|'
    sub_urls_list = sub_urls.split('|')
    for sub_url in sub_urls_list:
        # Special case for home page
        if sub_url == 'bulletin' and request.path == '/':
            return 'active'
        # Contains comparison is trigger by brackets
        if '(' in sub_url and ')' in sub_url:
            if sub_url[1:-1] in request.path:
                return 'active'
        else:
            if '/%s/' % sub_url == request.path:
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
