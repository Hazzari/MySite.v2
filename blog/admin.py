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
    list_display = ('id', 'title', 'slug', 'author', 'content', 'created_at', 'get_photo', 'views', 'category',)
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content')
    # empty_value_display = '-empty-'
    list_filter = ('category', 'tags')
    fields = ('get_photo', 'title', 'slug', 'author', 'content', 'created_at', 'photo', 'views', 'category', 'tags')
    readonly_fields = ('get_photo', 'views', 'created_at',)

    form = PostAdminForm

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')

    get_photo.short_description = 'Миниатюра'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    prepopulated_fields = {'slug': ('title',)}
