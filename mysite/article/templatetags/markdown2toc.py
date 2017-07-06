import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def markdown2toc(markdown_text):
    md = markdown.Markdown(extensions=['markdown.extensions.fenced_code', 'markdown.extensions.toc'])
    md.convert(markdown_text)
    toc = md.toc
    return mark_safe(toc)
