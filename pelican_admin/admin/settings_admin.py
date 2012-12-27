__author__ = 'Flavio'

from django.contrib import admin

from ..models import Settings

class SettingsAdmin(admin.ModelAdmin):
    fields = ['name', 'value',]
    list_display = ['name', 'value',]
    ordering = ['name',]
    search_fields = ['name', 'value',]

    actions = None

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name']

        return []

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Settings, SettingsAdmin)