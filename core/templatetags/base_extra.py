import re
from django import template
from datetime import datetime
from django.utils.datastructures import SortedDict
from core.constants import SKILL_RATING


register = template.Library()


@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return 'active'
    return ''


@register.simple_tag
def user_rating(widget_rating, skill_rating):
    if widget_rating == int(skill_rating):
        return 'active'
    else:
        return ''


@register.simple_tag
def rating_display(rating):
    return dict(SKILL_RATING)[rating]


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


@register.filter(name='percentage')
def percentage(value):
    return unicode(round(value * 100, 2)) + '%'


@register.simple_tag
def current_year():
    return unicode(datetime.now().year)
