__author__ = 'flaviocaetano'

from django.core.management.base import BaseCommand
from django.db.utils import DatabaseError
from django.conf import settings

class Command(BaseCommand):
    help = 'Import a blog to pelican_admin'
    can_import_settings = True

    def handle(self, *args, **options):
        try:
            from pelican_admin.models import Settings, BlogPost

            if settings.PELICAN_PATH:
                Settings.load_from_path()
                BlogPost.load_posts()
        except ImportError, e:
            self.stderr(e)
        except DatabaseError, e:
            self.stderr(e)