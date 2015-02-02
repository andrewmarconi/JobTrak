from django.conf.urls import patterns, include, url
from mmg.jobtrak.core import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
    url(r'^joblistings/$', views.job_list, name="job_list"),
    url(r'^contacts/$', views.contact_list, name="contact_list"),
    url(r'^jobboards/$', views.link_list, name="link_list"),
)
