from docutils.nodes import description

__author__ = 'flaviocaetano'

from django.conf import settings

def get_pelican_settings_file():
    return getattr(settings, 'PELICAN_SETTINGS', 'pelicanconf')