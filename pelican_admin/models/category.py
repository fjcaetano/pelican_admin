__author__ = 'flaviocaetano'

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        app_label = 'pelican_admin'
        ordering = ('name',)

        verbose_name = _('Category')
        verbose_name_plural = _('Categories')