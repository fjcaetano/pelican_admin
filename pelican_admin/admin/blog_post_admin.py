__author__ = 'Flavio'

from pelican_admin.models.blog_post import BlogPost, STATUS

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin, messages
from django import forms
from actions import delete_selected

from django_markdown.widgets import MarkdownWidget

def save_status(status):
    def action(self, request, queryset):
        rows_updated = BlogPost.objects.filter(id__in=list(bp.id for bp in queryset)).update(status=STATUS[status][0])
        dict = {'count': rows_updated, 'status': STATUS[status][1]}

        if rows_updated == 1:
            self.message_user(request, _('%(count)s blog post marked as %(status)s') % dict)
        else:
            self.message_user(request, _('%(count)s blog posts marked as %(status)s') % dict)

    action.short_description = _('Save all as %s') % STATUS[status][1]
    action.__name__ = 'set_status_%d' % status
    return action

class BlogPostForm(forms.ModelForm):
    text = forms.CharField(widget=MarkdownWidget())

    class Meta:
        model = BlogPost

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
    form = BlogPostForm
    actions = [delete_selected,] + list(save_status(status) for status in range(0, len(STATUS)))

    def get_readonly_fields(self, request, obj=None):
        return ['file_path']

    def delete_model(self, request, obj):
        try:
            obj.delete()
        except OSError, e:
            messages.error(request, e.strerror)

admin.site.register(BlogPost, BlogPostAdmin)