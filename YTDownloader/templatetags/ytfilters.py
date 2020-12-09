from django import template
register = template.Library()
@register.filter
def split(value,arg):
    value = value.split(arg)[0]
    value = value.split("/")[1]
    return value