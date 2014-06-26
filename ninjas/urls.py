from django.conf.urls import patterns, url

from ninjas import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<ninja_id>\d+)$', views.detail, name = 'detail'),
    url(r'^add$', views.NinjaCreate.as_view(), name = 'add'),
    url(r'^update/(?P<pk>\d+)$', views.NinjaUpdate.as_view(), name = 'update'),
)