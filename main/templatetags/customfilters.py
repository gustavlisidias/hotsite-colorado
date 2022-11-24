from django import template

register = template.Library()
@register.filter(is_safe=True)
def embed(value):
    return value[32:]