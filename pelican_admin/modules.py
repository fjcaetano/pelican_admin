__author__ = 'flaviocaetano'

from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules

import psutil

class PelicanAdmin(modules.DashboardModule):
    """Dashboard module for Pelican service administration.
    """

    title = 'Pelican Admin'

    template = 'pelican_admin.html'

    def __init__(self, *args, **kwargs):
        super(PelicanAdmin, self).__init__(*args, **kwargs)
        self.pelican_status = False

        for p in psutil.process_iter():
            try:
                if "pelican" in str(p.cmdline).lower():
                    self.pelican_status = True
                    break
            except psutil.AccessDenied, e:
                pass

    def is_empty(self):
        return False