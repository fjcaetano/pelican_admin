__author__ = 'flaviocaetano'
__VERSION__ = 0.3

from django.conf import settings, urls

from pelican_admin.helper import get_pelican_settings_file

import django, os, signal, atexit

def pelican_urls():
    """Helper function to return a URL pattern for serving pelican_admin webservices.
    """

    return (
        urls.url(r'^admin/pelican/', urls.include('pelican_admin.urls')),
        urls.url(r'^admin/jsi18n.js$', 'django.views.i18n.javascript_catalog', {'packages': 'pelican_admin'}),
        urls.url(r'^admin/pelican_blog/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PELICAN_PATH, 'output')}),
    )

def _kill_pelican_service():
    print 'Killing pelican services'

    import psutil
    for p in psutil.process_iter():
        try:
            if "pelican" in str(p.cmdline).lower():
                os.kill(p.pid, signal.SIGKILL)
        except psutil.AccessDenied, e:
            pass

def _start_pelican_service():
    pelican_settings_name = get_pelican_settings_file()
    pelican = getattr(settings, 'PELICAN_BIN', '/usr/local/bin/pelican')

    cmdline = pelican+' -s %s.py -r &' % pelican_settings_name
    os.chdir(settings.PELICAN_PATH)
    os.system(cmdline)

def _check_pelican_service():
    status = False

    import psutil
    for p in psutil.process_iter():
        try:
            if "pelican" in str(p.cmdline).lower():
                status = True
                break
        except psutil.AccessDenied, e:
            pass

    return status


# Beginning
try:
    from pelican_admin.models import Settings, BlogPost

    if settings.PELICAN_PATH:
        settings.LOCALE_PATHS = settings.LOCALE_PATHS + ('pelican_admin.locale',)
        settings.INSTALLED_APPs = settings.INSTALLED_APPS + ('djangotoolbox',)

        Settings.load_from_path()
        BlogPost.load_posts()

        _start_pelican_service()
        atexit.register(_kill_pelican_service)
except ImportError, e:
    print e
except django.db.utils.DatabaseError, e:
    print e