__author__ = 'flaviocaetano'

"""A basic database set-up for Travis CI.

The set-up uses the 'TRAVIS' (== True) environment variable on Travis
to detect the session, and changes the default database accordingly.

Be mindful of where you place this code, as you may accidentally
assign the default database to another configuration later in your code.
"""

import os

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