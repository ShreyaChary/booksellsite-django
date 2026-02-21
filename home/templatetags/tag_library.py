from django import template

register = template.Library()

@register.filter
def to_int_progress(value):
    try:
        return int(value)
    except:
        return 0
