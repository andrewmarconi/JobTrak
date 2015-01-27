from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

urlpatterns = i18n_patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('mmg.jobtrak.core.urls')),
    url(r'^$', include('mmg.jobtrak.public.urls')),
)

