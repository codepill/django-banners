from django.template import Library, Node, TemplateSyntaxError
from banners.models import Slot
import re

register = Library()

class BannersForSlotNode(Node):
    def __init__(self, symbol, cast_as=None, options=None):
        self.symbol = symbol
        self.cast_as = cast_as
        self.options = options

    def render(self, context):
        try:
            slot = Slot.objects.get(symbol=self.symbol, language=context['LANGUAGE_CODE'])
            banners = slot.published_banners
            limit = self.options.get('limit') or slot.limit
            banners = banners[:limit]
            if self.cast_as:
                context[self.cast_as] = banners
                return ''
            return banners
        except Slot.DoesNotExist:
            return ''


@register.tag
def banners_for_section(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)  # Splitting by None == splitting by spaces.
    except ValueError:
        raise TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]
    correct_tag_syntax = re.search(r'^(.*?) as (\w+)(.*)$', arg)
    if not correct_tag_syntax:
        raise TemplateSyntaxError, "The %(tag_name)r tag syntax is incorrect. " \
                                   "Correct syntax is '%(tag_name)s slot as variable' " \
                                   "where 'variable' can be any name." % {'tag_name': tag_name}
    else:
        symbol, cast_as, opts = correct_tag_syntax.groups()
        opts_dict = {}
        for opt in opts.split(' '):
            if opt.find('=') == -1:
                opts_dict[opt] = True
            else:
                name, value = opt.split('=')
                opts_dict[str(name)] = value
        return BannersForSlotNode(symbol, cast_as, opts_dict)
