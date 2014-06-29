from django.conf.urls import patterns, url

from dashboard import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name = 'index'),
    url(r'^$', views.index, name = 'index'),
    # url(r'^(?P<mentor_id>\d+)/$', views.detail, name = 'detail'),
)