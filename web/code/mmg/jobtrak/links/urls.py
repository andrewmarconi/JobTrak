from django.conf.urls import include, url, i18n
from mmg.jobtrak.links import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
