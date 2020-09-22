from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.shortcuts import render

from blog.models import Post, Category, Tag


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog-home.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог'
        return context


# TODO: Поменять на DetailView
class BlogPostView(TemplateView):
    template_name = 'blog/blog-post.html'


def get_category(request, slug):
    return render(request, 'blog/category.html', )
