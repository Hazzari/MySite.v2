from django.views.generic import ListView, DetailView
from django.db.models import F

from blog.models import Post, Category, Tag


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog-home.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог'
        return context


class PostByCategoryView(ListView):
    template_name = 'blog/blog-home.html'
    context_object_name = 'posts'
    paginate_by = 6
    allow_empty = False  # 404 на несуществующий обьект вместо ошибки сервера

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostByTagView(ListView):
    template_name = 'blog/blog-home.html'
    context_object_name = 'posts'
    paginate_by = 6
    allow_empty = False  # 404 на несуществующий обьект вместо ошибки сервера

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу: ' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context


class BlogPostView(DetailView):
    model = Post
    template_name = 'blog/blog-post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context
