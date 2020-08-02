from django import template

register = template.Library()


@register.inclusion_tag('zenofewords/tags/external_link_tag.html')
def external_link_tag(url, title, terminator):
    return {
        'url': url,
        'title': title,
        'terminator': terminator,
    }


@register.inclusion_tag('zenofewords/tags/mobile_menu_link_tag.html')
def mobile_menu_link_tag(name, path):
    return {
        'name': name,
        'current': name in path or name == 'home' and '/' == path,
    }
