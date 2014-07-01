from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name = 'index'),
    url(r'^login?/$', views.login, name = 'login'),
    url(r'^logout?/$', views.logout, name = 'logout'),
    url(r'^permissions$', views.permissions, name = 'permissions'),
    url(r'^cp$', views.cp, name = 'cp'),
    # url(r'^(?P<mentor_id>\d+)/$', views.detail, name = 'detail'),
)