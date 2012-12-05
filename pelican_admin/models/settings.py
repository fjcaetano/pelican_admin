__author__ = 'Flavio'

from django.db import models
from django.conf import settings

import os, sys, pprint

from pelican_admin import get_pelican_settings

from pelican import settings as ps

class Settings(models.Model):

    name = models.CharField(max_length=32, unique=True, primary_key=True)

    value = models.TextField()

    def save(self, **kwargs):
        super(Settings, self).save(**kwargs)

        pelican_settings_name = get_pelican_settings()
        f = open(os.path.join(settings.PELICAN_PATH, pelican_settings_name+'.py'), 'w')

        f.write('#coding: utf-8\n\n')

        all_objs = Settings.objects.all()

        for set in all_objs:
            f.write('%s = %s\n' % (set.name, set.value))

        f.close()

    @classmethod
    def load_from_path(cls):
        pelican_settings_name = get_pelican_settings()

        sys.path.append(settings.PELICAN_PATH)
        pelican_settings = None

        exec 'import %s; pelican_settings = %s' % (pelican_settings_name, pelican_settings_name) in None

        attr_list = dir(pelican_settings)
        user_settings = dict((attr, getattr(pelican_settings, attr)) for attr in attr_list if not attr.startswith('__'))

        default = dict(ps._DEFAULT_CONFIG.items() + user_settings.items())

        for attr, def_value in default.items():
            attr_value = pprint.pformat(def_value)

            set = Settings(name=attr, value=attr_value)
            set.save()

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name_plural = 'Settings'
        ordering = ['name']
        app_label = 'pelican_admin'