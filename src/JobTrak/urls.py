from django.conf.urls import include, url, i18n
#from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from JobTrak.admin import JobTrakAdmin

urlpatterns = i18n.i18n_patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^manager/doc/', include('django.contrib.admindocs.urls')),
    url(r'^manager/', include (JobTrakAdmin.urls)),
    url(r'^app/', include('mmg.jobtrak.core.urls', namespace='core')),
    url(r'^$', include('mmg.jobtrak.public.urls')),
)
