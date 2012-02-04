from django import template
from django.core.urlresolvers import reverse
from datetime import datetime

register = template.Library()

@register.simple_tag
def active(request, urls):
    if request.path in (reverse(url) for url in urls.split()):
        return "active"
    return ""

@register.simple_tag
def current_year():
    return unicode(datetime.now().year)