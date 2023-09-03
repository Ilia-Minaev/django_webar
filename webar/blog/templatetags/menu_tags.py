from django import template
from blog.models import Page
register = template.Library()


@register.inclusion_tag('blog/tags/menu.html', takes_context=True)
def show_top_menu(context):
    menu_items = Page.objects.all()
    return {
        "menu_items": menu_items,
    }
