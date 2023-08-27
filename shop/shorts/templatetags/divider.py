from django import template

register = template.Library()

@register.filter
def divide(value, arg):
    try:
        return float('{:.2f}'.format(int(value) / int(arg)))
    except (ValueError, ZeroDivisionError):
        return None
    

@register.filter
def multiply(value, arg):
    return int(value) * int(arg)