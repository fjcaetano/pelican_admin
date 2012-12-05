__author__ = 'Flavio'

from pelican_admin.models.blog_post import BlogPost, MARKUPS

from django.contrib import admin

class BlogPostAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return ['file_path']

admin.site.register(BlogPost, BlogPostAdmin)