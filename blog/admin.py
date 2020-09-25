from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'created_at',
        'get_photo',
        'views',
        'category',
        'is_published',
        'status')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content')
    save_on_top = True
    view_on_site = True
    actions_on_bottom = True
    actions_on_top = False
    empty_value_display = '-empty-'
    list_filter = ('category', 'tags')
    date_hierarchy = 'created_at'
    fields = ('get_photo',
              'title',
              'slug',
              'author',
              'content',
              'created_at',
              'photo',
              'views',
              'category',
              'tags')
    readonly_fields = ('get_photo',
                       'views',
                       'created_at',)

    form = PostAdminForm

    def get_photo(self, obj):
        """Миниатюра в админке"""
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')

    get_photo.short_description = 'Миниатюра'  # название столбца


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    prepopulated_fields = {'slug': ('title',)}
