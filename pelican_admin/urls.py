__author__ = 'flaviocaetano'

from django.contrib.admin import site
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

import os, time

from pelican_admin import _kill_pelican_service, _start_pelican_service, _check_pelican_service
from pelican_admin.models import BlogPost
from pelican_admin.admin.blog_post_admin import BlogPostAdmin

@csrf_exempt
def service_action(request):
    status = int(request.GET['status']) != 0
    callback = request.GET['callback']

    # Stop pelican services
    _kill_pelican_service()

    if not status:
        # Start pelican
        _start_pelican_service()

    time.sleep(1)

    new_status = int(_check_pelican_service())

    return HttpResponse('%s(%s)' % (callback, new_status))

@csrf_exempt
def view_draft(request):
    blog_form = BlogPostAdmin(BlogPost, site)
    form = blog_form.get_form(request)(request.POST)

    form.is_valid()

    remove_later = False

    try:
        blog_post = BlogPost.get_from_meta(
            markup=form.cleaned_data.get('markup'),
            title=form.cleaned_data.get('title'),
            slug=form.cleaned_data.get('slug'))
    except BlogPost.DoesNotExist:
        remove_later = True
        blog_post = BlogPost()

    for key in form.cleaned_data.keys():
        setattr(blog_post, key, form.cleaned_data.get(key))

    blog_post.status = 'draft'
    blog_post.write()

    time.sleep(2)

    if remove_later:
        os.remove(blog_post.file_path)

    return HttpResponseRedirect('/admin/pelican_blog/drafts/%s.html' % blog_post.get_slug())

### URLS

from django.conf.urls import patterns, url

urls = (
    url(r'^service$', 'pelican_admin.urls.service_action'),
    url(r'view_draft$', 'pelican_admin.urls.view_draft'),
)

urlpatterns = patterns('', *urls)