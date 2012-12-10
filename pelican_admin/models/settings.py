__author__ = 'Flavio'

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import simplejson

import os, sys, pprint, unicodedata, ast

from pelican_admin.helper import get_pelican_settings_file

from pelican import settings as ps

class Settings(models.Model):
    name = models.CharField(_('Name'), max_length=32, unique=True, primary_key=True)

    value = models.TextField(_('Value'), blank=True, default='')

    def save(self, **kwargs):
        super(Settings, self).save(**kwargs)

        self.write()

    def write(self):
        pelican_settings_name = get_pelican_settings_file()
        f = open(os.path.join(settings.PELICAN_PATH, pelican_settings_name+'.py'), 'w+')

        f.write('#coding: utf-8\n\n')

        all_objs = Settings.objects.all()

        for set in all_objs:
            value = set.value
            try:
                value = ast.literal_eval(value)
            except Exception:
                value = simplejson.dumps(value)

            f.write('%s = %s\n' % (set.name, value))

        f.close()

    @classmethod
    def load_from_path(cls):
        Settings.objects.all().delete()

        pelican_settings_name = get_pelican_settings_file()

        sys.path.append(settings.PELICAN_PATH)
        pelican_settings = None

        exec 'import %s; pelican_settings = %s' % (pelican_settings_name, pelican_settings_name) in None

        attr_list = dir(pelican_settings)
        user_settings = dict((attr, getattr(pelican_settings, attr)) for attr in attr_list if not attr.startswith('__'))

        default = dict(ps._DEFAULT_CONFIG.items() + user_settings.items())

        settings_list = []

        for attr, def_value in default.items():
            if isinstance(def_value, str):
                attr_value = def_value
            elif isinstance(def_value, unicode):
                attr_value = unicodedata.normalize('NFKD', def_value).encode('ascii', 'ignore')
            else:
                attr_value = pprint.pformat(def_value)

            set = Settings(name=attr, value=attr_value)
            settings_list.append(set)

        Settings.objects.bulk_create(settings_list)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _('Setting')
        verbose_name_plural = _('Settings')

        ordering = ['name']
        app_label = 'pelican_admin'