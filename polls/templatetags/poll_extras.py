from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter(needs_autoescape=False)
def cut(text, autoescape=False):
    first, other = text[0], text[1:]
    esc = lambda x: x
    result = re.sub('\r?\n', ' <br> ', text)
    return mark_safe(result)