# -*- coding: utf-8 -*-
import re

from django import template
from django.conf import settings
from django.template import Variable
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.template import RequestContext

register = template.Library()

# http://stackoverflow.com/a/9250304
@register.filter
def tabindex(value, index):
    """
    Add a tabindex attribute to the widget for a bound field.
    """
    value.field.widget.attrs['tabindex'] = index
    return value

@register.filter
def rootdomain(value):
    """
    Get root domain of a link
    """
    # return re.match(value.split())
    value = re.search("(?<=\/\/)(.*?)(?=\/)", value)
    if value:
        # return "value.group() : ", value.group()
        return value.group(1)
    else:
        return ""
    # url = value
    # value = url
    # value = urlparse.urlparse(url).value.split(".")
    # value = ".".join(len(value[-2]) < 4 and value[-3:] or value[-2:])