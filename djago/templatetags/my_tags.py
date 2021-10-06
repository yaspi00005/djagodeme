from django import template

register = template.Library()

@register.filter
def modulo(num, val):
    return num % val

@register.filter(is_safe=True)
def reste(chaine):
    if len(chaine) > 1: return chaine[1:]
    return chaine