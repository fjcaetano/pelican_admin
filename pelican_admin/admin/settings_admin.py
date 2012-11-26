__author__ = 'Flavio'

from django.contrib import admin

from ..models import Settings

class SettingsAdmin(admin.ModelAdmin):
    fields = ['name', 'value']
    actions = None

    def get_readonly_fields(self, request, obj=None):
        return ['name']

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(Settings, SettingsAdmin)