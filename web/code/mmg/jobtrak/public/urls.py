from django.conf.urls import include, url
from mmg.jobtrak.public import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
