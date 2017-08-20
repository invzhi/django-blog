import markdown

from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def md2html(markdown_text):
    html = markdown.markdown(
        markdown_text,
        output_format='html5',
        extensions=[
            'markdown.extensions.abbr',
            'markdown.extensions.fenced_code',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )
    return mark_safe(html)
