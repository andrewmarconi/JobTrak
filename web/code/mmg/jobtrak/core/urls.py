from django.conf.urls import patterns, include, url, i18n
from mmg.jobtrak.core import views

urlpatterns = [
    url(r'^joblistings/$', views.job_list, name="job_list"),
    url(r'^joblistings/(?P<id>[0-9]+)/$', views.job_detail, name='job_detail'),
    url(r'^$',views.index,name='index'),
]
