from django import template

from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag(filename='blog/popular_post_tpl.html')
def get_popular(name_post: str, cnt=3) -> dict:
    """
    показываем популярные статьи за исключением открытой
    """
    print(f'name_post = {name_post}')
    posts = Post.objects.order_by('-views').exclude(slug__exact=name_post)[:cnt]
    return {'posts': posts}


@register.inclusion_tag(filename='blog/tags_tpl.html')
def get_tags() -> dict:
    """
    показываем теги
    """
    tags = Tag.objects.all()
    return {'tags': tags}
