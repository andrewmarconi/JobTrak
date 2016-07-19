from django.conf.urls import include, url, i18n
#from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from JobTrak.admin import JobTrakAdmin

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include (JobTrakAdmin.urls)),
]

urlpatterns += i18n.i18n_patterns(
    url(r'^app/contact/', include('mmg.jobtrak.contact.urls', namespace='contact')),
    url(r'^app/', include('mmg.jobtrak.core.urls', namespace='core')),
    url(r'^', include('mmg.jobtrak.public.urls')),
)
