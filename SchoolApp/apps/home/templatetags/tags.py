from django import template
from django.templatetags import static

register = template.Library()


# used in classes_view.html
@register.filter
def length_active(assignments):
    return len([1 for x in assignments if x.is_active()])


# COPIED FROM https://stackoverflow.com/a/47336360/12451222
class FullStaticNode(static.StaticNode):
    def url(self, context):
        request = context['request']
        return request.build_absolute_uri(super().url(context))


# used in base.html
@register.tag('fullstatic')
def do_static(parser, token):
    return FullStaticNode.handle_token(parser, token)
