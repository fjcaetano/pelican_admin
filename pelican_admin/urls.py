__author__ = 'flaviocaetano'

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import psutil, os, signal, time, subprocess, shlex

from pelican_admin import get_pelican_settings

@csrf_exempt
def service_action(request):
    status = int(request.GET['status']) != 0
    callback = request.GET['callback']

    # Stop pelican Services
    for p in psutil.process_iter():
        try:
            if "pelican" in str(p.cmdline).lower():
                os.kill(p.pid, signal.SIGKILL)
        except psutil.AccessDenied, e:
            pass

    if not status:
        # Start pelican
        pelican_settings_name = get_pelican_settings()
        pelican = getattr(settings, 'PELICAN_BIN', '/usr/local/bin/pelican')

        cmdline = pelican+' -s %s.py -r &' % pelican_settings_name
        os.chdir(settings.PELICAN_PATH)
        os.system(cmdline)

    time.sleep(2)

    new_status = 0
    for p in psutil.process_iter():
        try:
            if "pelican" in str(p.cmdline).lower():
                new_status = 1
                break
        except psutil.AccessDenied, e:
            pass

    return HttpResponse('%s(%s)' % (callback, new_status))

### URLS

from django.conf.urls import patterns, url

urls = (
    url(r'^$', 'pelican_admin.urls.service_action'),
)

urlpatterns = patterns('', *urls)