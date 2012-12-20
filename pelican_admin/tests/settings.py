from django.conf.project_template.project_name.settings import ROOT_URLCONF

__author__ = 'flaviocaetano'

"""A basic database set-up for Travis CI.

The set-up uses the 'TRAVIS' (== True) environment variable on Travis
to detect the session, and changes the default database accordingly.

Be mindful of where you place this code, as you may accidentally
assign the default database to another configuration later in your code.
"""

import os
BASE_PATH = os.path.dirname(__file__)

if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pelican_admin_test',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        },
    }

SITE_ID = 1

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'pelican_admin',
]

PELICAN_PATH = os.path.join(BASE_PATH, 'blog/')

ROOT_URLCONF = 'pelican_admin.tests.urls'