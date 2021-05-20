from django import template

register = template.Library()


@register.filter('endswith')
def endswith(text, string):
    if isinstance(text, str):
        return text.endswith(string)
    return False
