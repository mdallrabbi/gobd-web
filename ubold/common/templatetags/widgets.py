import json

from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('widgets/profile-widget.html')
def user_profile(*args, **kwargs):
    stats = kwargs.pop('stats')
    stats = str(stats).replace("'", '"')
    try:
        kwargs['stats'] = json.loads(stats)
    except json.decoder.JSONDecodeError:
        pass
    return kwargs


@register.inclusion_tag('widgets/stat-widget.html')
def stat(*args, **kwargs):
    return kwargs
