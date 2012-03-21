from django import template
from datetime import datetime
from django.conf import settings
from crowd.forms import EncouragementForm
from backstage.forms import ReportForm
from django.utils.datastructures import SortedDict

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


@register.filter(name='sort')
def structsort(value):
    if isinstance(value, dict):
        new_dict = SortedDict()
        key_list = value.keys()
        key_list.sort()
        for key in key_list:
            new_dict[key] = value[key]
        return new_dict
    elif isinstance(value, list):
        new_list = list(value)
        new_list.sort()
        return new_list
    else:
        return value
    structsort.is_safe = True


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
