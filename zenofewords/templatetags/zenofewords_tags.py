from django import template

register = template.Library()


@register.inclusion_tag('zenofewords/tags/external_link_tag.html')
def external_link_tag(url, title, terminator=''):
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


@register.inclusion_tag('zenofewords/tags/jump_to_link_tag.html')
def jump_to_link_tag(css_class, aria_label, url='#top'):
    return {
        'css_class': css_class,
        'aria_label': aria_label,
        'url': url,
    }


@register.inclusion_tag('zenofewords/tags/content_block_tag.html')
def content_block_tag():
    return {}
