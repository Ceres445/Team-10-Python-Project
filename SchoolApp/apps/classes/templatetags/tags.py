from django import template

register = template.Library()


@register.filter
def length_active(assignments):
    return len([1 for x in assignments if x.is_active()])
