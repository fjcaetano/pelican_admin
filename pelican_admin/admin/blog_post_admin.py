__author__ = 'Flavio'

from pelican_admin.models.blog_post import BlogPost

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

class BlogPostAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields' : ('title', 'markup', 'lang', 'summary', 'text', 'date',),
            }),
        (_('Extra Info'), {
            'classes': ['collapse'],
            'fields': ('slug', 'tags', 'category', 'author', 'status', 'file_path',),
            }),
    )

    list_display = ('title', 'markup', 'lang', 'status', 'date',)
    ordering = ('-date', 'title')
    list_filter = ('category', 'status',)
    search_fields = ('title', 'text', 'tags', 'category__name')
    date_hierarchy = 'date'

    def get_readonly_fields(self, request, obj=None):
        return ['file_path']

admin.site.register(BlogPost, BlogPostAdmin)