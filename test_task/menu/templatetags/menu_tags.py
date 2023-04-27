from django import template
from menu.models import MenuItem
from mptt.querysets import TreeQuerySet

register = template.Library()


@register.simple_tag()
def get_menu_objects() -> TreeQuerySet:
    return MenuItem.objects.filter(level=0).all()
