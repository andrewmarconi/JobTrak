from django.conf.urls import patterns, include, url
from mmg.jobtrak.core import views

urlpatterns = [
    url(r'^joblistings/$', views.job_list, name="job_list"),
    url(r'^$',views.index,name='index'),
]
