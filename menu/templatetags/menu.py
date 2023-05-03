from django import template
from django.core.exceptions import ObjectDoesNotExist

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name):
    menu = MenuItem.objects.filter(
        menu__name=name
    )
    request = context.get('request')

    try:
        active_menu_item = menu.get(slug=request.path[1:])
    except ObjectDoesNotExist:
        level = 1
        active_menu_item = None
    else:
        level = active_menu_item.level

    menu = [menu_item for menu_item in menu if menu_item.level <= level]
    if active_menu_item:
        menu += active_menu_item.children.all()
    menu = sorted(
        menu, key=lambda menu_item: (menu_item.level, menu_item.name)
    )
    return {'active_menu_item': active_menu_item, 'menu': menu}
