from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Категория постов записей блога
    """
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=250, unique=True)

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    """
    Теги постов записей блога
    """
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    """
    Посты блога
    """
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликована'),
    )

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликованно')
    photo = models.ImageField(upload_to='photo/%Y/%m/%/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts', )
    tags = models.ManyToManyField(to=Tag, related_name='posts', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Статус', )
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='draft', )

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
