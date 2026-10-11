import re

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

TOKEN = re.compile(
    r"(?P<c>#[^\n]*)"
    r'|(?P<s>"[^"\n]*")'
    r"|(?P<k>\b(?:def|class|for|in|from|import|return|zip)\b)"
    r"|(?P<n>\b\d+(?:\.\d+)?\b)"
    r"|(?P<f>\b[A-Za-z_]\w*(?=\())"
)


def _highlight_line(line):
    out, pos = [], 0
    for match in TOKEN.finditer(line):
        out.append(escape(line[pos : match.start()]))
        out.append(f'<span class="t-{match.lastgroup}">{escape(match.group())}</span>')
        pos = match.end()
    out.append(escape(line[pos:]))
    return "".join(out)


@register.filter
def code_lines(source):
    """Render source as one <span class="ln"> per line with light syntax colouring."""
    lines = source.strip("\n").split("\n")
    html = "".join(
        f'<span class="ln" style="--i:{i}">{_highlight_line(line) or "&nbsp;"}</span>'
        for i, line in enumerate(lines)
    )
    return mark_safe(html)
