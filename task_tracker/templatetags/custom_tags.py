from django import template

register = template.Library()

@register.filter(name="endwith")
def endwith(value, arg):
    return value.lower().endwith(arg.lower())