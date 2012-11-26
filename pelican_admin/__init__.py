__author__ = 'flaviocaetano'

__VERSION__ = 0.1

from django.conf import settings
import django

try:
    from models import Settings, BlogPost

    if settings.PELICAN_PATH:
        Settings.load_from_path()
        BlogPost.load_posts()
except ImportError, e:
    pass
except django.db.utils.DatabaseError, e:
    pass