from django import template
from django.db.models import Count

from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag(filename='blog/popular_post_tpl.html')
def get_popular(name_post: str, cnt=3) -> dict:
    """
    показываем популярные статьи за исключением открытой
    """
    posts = Post.objects.order_by('-views').exclude(slug__exact=name_post)[:cnt]
    return {'posts': posts}


@register.inclusion_tag(filename='blog/tags_tpl.html')
def get_tags() -> dict:
    """
    показываем теги
    """
    tags = Tag.objects.annotate(count_posts=Count('posts')).filter(count_posts__gt=0)
    return {'tags': tags}
