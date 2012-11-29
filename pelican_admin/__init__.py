__author__ = 'flaviocaetano'

__VERSION__ = 0.2

from django.conf import settings, urls
import django

try:
    from pelican_admin.models import Settings, BlogPost

    if settings.PELICAN_PATH:
        Settings.load_from_path()
        BlogPost.load_posts()
except ImportError, e:
    pass
except django.db.utils.DatabaseError, e:
    pass

def pelican_urls():
    """Helper function to return a URL pattern for serving pelican_admin webservices.
    """

    return (
        urls.url(r'^pelican_admin/', urls.include('pelican_admin.urls')),
        urls.url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': 'pelican_admin'}),
    )

def get_pelican_settings():
    return getattr(settings, 'PELICAN_SETTINGS', 'pelicanconf')