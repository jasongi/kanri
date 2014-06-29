from django.conf.urls import patterns, url

from mentors import views

urlpatterns = patterns('',
    # url(r'^$', 'views.home', name='home'),
    url(r'^$', views.index, name = 'index'),
    url(r'^add$', views.add, name = 'add'),
    url(r'^(?P<mentor_id>\d+)/$', views.detail, name = 'detail'),
)