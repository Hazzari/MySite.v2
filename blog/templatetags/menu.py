from django import template
from django.db.models import Count

from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/menu_tpl.html')
def show_menu():
    """
    получение категорий меню в которых есть записи
    """
    categories = Category.objects.annotate(count_category=Count('posts')).filter(count_category__gt=0)
    return {'categories': categories}
