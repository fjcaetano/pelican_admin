__author__ = 'flaviocaetano'

from django.core.management.base import BaseCommand
from django.db.utils import DatabaseError
from django.conf import settings

class Command(BaseCommand):
    help = 'Import a blog to pelican_admin'
    can_import_settings = True

    def handle(self, *args, **options):
        try:
            self.stdout.write('Starting import of pelican blog\n')
            from pelican_admin.models import Settings, BlogPost

            if settings.PELICAN_PATH:
                self.stdout.write('Importing settings\n')
                Settings.load_from_path()

                self.stdout.write('Importing blog posts\n')
                BlogPost.load_posts()

            self.stdout.write('Finished importing pelican blog\n')
        except ImportError, e:
            self.stderr.write(e)
        except DatabaseError, e:
            self.stderr.write(e)