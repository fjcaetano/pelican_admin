__author__ = 'flaviocaetano'

from django.conf import settings
from django.contrib.admin import site
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import psutil, os, signal, time, urlparse, pprint

from pelican_admin import get_pelican_settings
from pelican_admin.models import BlogPost, Settings
from pelican_admin.admin.blog_post_admin import BlogPostAdmin

from pelican.utils import slugify

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

@csrf_exempt
def view_draft(request):
    blog_form = BlogPostAdmin(BlogPost, site)
    form = blog_form.get_form(request)(request.POST)

    form.is_valid()

    blog_post = BlogPost()

    blog_post.title = form.cleaned_data.get('title')
    blog_post.markup = form.cleaned_data.get('markup')
    blog_post.text = form.cleaned_data.get('text')
    blog_post.date = form.cleaned_data.get('date')
    blog_post.file_path = form.cleaned_data.get('file_path')

    blog_post.text = '%s: draft\n%s' % (blog_post.metafy('status'), blog_post.text)

    blog_post.write()

    site_url = Settings.objects.get(name='SITEURL')
    site_url = site_url.value.replace("'", '')

#    return HttpResponseRedirect(urlparse.urljoin(site_url, 'drafts/%s.html' % slugify(blog_post.title)))
    return HttpResponseRedirect('/pelican_blog/drafts/%s.html' % slugify(blog_post.title))

### URLS

from django.conf.urls import patterns, url

urls = (
    url(r'^$', 'pelican_admin.urls.service_action'),
    url(r'view_draft$', 'pelican_admin.urls.view_draft'),
)

urlpatterns = patterns('', *urls)