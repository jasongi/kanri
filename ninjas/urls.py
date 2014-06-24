from django.conf.urls import patterns, url

from ninjas import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<ninja_id>\d+)/$', views.detail, name = 'detail'),
)