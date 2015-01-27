from django.conf.urls import patterns, include, url
from mmg.jobtrak.core import views

urlpatterns = patterns('',
    url(r'^$',views.index,name='index'),
)