__author__ = 'flaviocaetano'
__VERSION__ = 0.3

from django.conf import urls

from pelican_admin.helper import get_pelican_settings_file, KThread

from pelican import main as pelican_main, settings as ps

import os, sys, atexit, threading

def pelican_urls():
    """Helper function to return a URL pattern for serving pelican_admin webservices.
    """

    return (
        urls.url(r'^admin/markdown/', urls.include('django_markdown.urls')),
        urls.url(r'^admin/pelican/', urls.include('pelican_admin.urls')),
        urls.url(r'^admin/jsi18n.js$', 'django.views.i18n.javascript_catalog', {'packages': 'pelican_admin'}),
        urls.url(r'^admin/pelican_blog/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PELICAN_PATH, 'output')}),
    )

def _kill_pelican_service():
    for thread in threading.enumerate():
        if thread.name == 'pelican_thread':
            thread.kill()

def _start_pelican_service():
    from django.conf import settings

    def substart():
        pelican_settings_name = get_pelican_settings_file()
        pelican_settings_path = os.path.join(settings.PELICAN_PATH, pelican_settings_name+'.py')

        pelican_main(settings.PELICAN_PATH, settings=pelican_settings_path, autoreload=True)

    if not _check_pelican_service():
        thread = KThread(target=substart, name='pelican_thread')
#        thread.setDaemon(True)
        thread.start()

def _check_pelican_service():
    status = 'pelican_thread' in list(thread.name for thread in threading.enumerate())

    return status


# Beginning
try:
    from django.conf import settings

    if settings.PELICAN_PATH:
        sys.path.append(settings.PELICAN_PATH)

        settings.LOCALE_PATHS += ('pelican_admin.locale',)
        settings.INSTALLED_APPS += ('django_markdown','django.contrib.markup', 'pelican',)

        settings.MARKDOWN_EDITOR_SKIN = getattr(settings, 'MARKDOWN_EDITOR_SKIN', 'simple')
        settings.DJANGO_MARKDOWN_STYLE = '/admin/pelican_blog/theme/' + ps._DEFAULT_CONFIG['CSS_FILE']

        atexit.register(_kill_pelican_service)
except ImportError, e:
    print e