from django.conf.urls import patterns, include, url
from mmg.jobtrak.contact import views

urlpatterns = [
    url(r'^view/(\d+)/$', views.contact_detail, name='contact_detail'),
    url(r'^$', views.contact_list, name='contact_list'),
]
