from django import template
import markdown

register = template.Library()

@register.filter
def markdownify(text):
    # safe_mode governs how the function handles raw HTML
    return markdown.markdown(text, safe_mode='escape')

@register.filter
def tag_to_list(text):
    # Converts a comma-separated string to a list.
    items = text.split(',')
    rv = "<ul>"
    for i in items:
        rv += "<li>{}</li>".format(i.strip(" "))
    rv += "</ul>"
    return rv
