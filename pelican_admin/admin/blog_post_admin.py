__author__ = 'Flavio'

from pelican_admin.models.blog_post import BlogPost, MARKUPS

from django.contrib import admin
from django.template.defaultfilters import slugify
from django.conf import settings

import os

class BlogPostAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return ['file_path']

    def save_model(self, request, obj, form, change):
        if not change:
            filename ='%s.%s' % (slugify(obj.title), MARKUPS[obj.markup][1])
            obj.file_path = os.path.join(settings.PELICAN_PATH, 'content', filename)

        obj.save()

admin.site.register(BlogPost, BlogPostAdmin)