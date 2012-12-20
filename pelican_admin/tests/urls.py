from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import pelican_admin

admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += pelican_admin.pelican_urls()
