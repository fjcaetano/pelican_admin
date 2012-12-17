__author__ = 'flaviocaetano'

from admin_tools.dashboard import modules

from pelican_admin.models import Settings

from . import _check_pelican_service

class PelicanAdmin(modules.DashboardModule):
    """Dashboard module for Pelican service administration.
    """

    title = 'Pelican Admin'

    template = 'pelican_admin.html'

    def __init__(self, *args, **kwargs):
        super(PelicanAdmin, self).__init__(*args, **kwargs)
        self.pelican_status = _check_pelican_service()

        try:
            self.blog_url = Settings.objects.get(name='SITEURL').value
        except Settings.DoesNotExist:
            self.blog_url = None

    def is_empty(self):
        return False