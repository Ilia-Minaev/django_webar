from django import template
from blog.models import Page
register = template.Library()


@register.inclusion_tag('blog/tags/header_menu.html', takes_context=True)
def show_header_menu(context):
    menu_items = Page.objects.all()
    return {"menu_items": menu_items,}

@register.inclusion_tag('blog/tags/footer_menu.html', takes_context=True)
def show_footer_menu(context):
    menu_items = Page.objects.all()
    return {"menu_items": menu_items,}

