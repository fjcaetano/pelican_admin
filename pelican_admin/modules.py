__author__ = 'flaviocaetano'

from admin_tools.dashboard import modules

from . import _check_pelican_service

class PelicanAdmin(modules.DashboardModule):
    """Dashboard module for Pelican service administration.
    """

    title = 'Pelican Admin'

    template = 'pelican_admin.html'

    def __init__(self, *args, **kwargs):
        super(PelicanAdmin, self).__init__(*args, **kwargs)
        self.pelican_status = _check_pelican_service()

    def is_empty(self):
        return False