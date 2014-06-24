from django.conf.urls import patterns, url

from attendance import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    # url(r'^(?P<mentor_id>\d+)/$', views.detail, name = 'detail'),
    url(r'^signoff/(?P<dojo_session_id>\d+)$', views.signoff, name = 'signoff'),
)