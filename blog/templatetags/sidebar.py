from django import template

from blog.models import Post

register = template.Library()


@register.inclusion_tag(filename='blog/popular_post_tpl.html')
def get_popular(name_post, cnt=3):
    """
    показываем популярные статьи за исключением открытой
    """
    posts = Post.objects.order_by('-views').exclude(slug__exact=name_post)[:cnt]
    return {'posts': posts}
