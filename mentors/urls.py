from django.conf.urls import patterns, url

from mentors import views

urlpatterns = patterns('',
    # url(r'^$', 'views.home', name='home'),
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<mentor_id>\d+)/$', views.detail, name = 'detail'),
    url(r'^add$', views.MentorCreate.as_view(), name = 'add'),
    url(r'^update/(?P<pk>\d+)$', views.MentorUpdate.as_view(), name = 'update'),
    url(r'^role$', views.role_index, name = 'role-index'),
    url(r'^role/add$', views.RoleCreate.as_view(), name = 'role-add'),
    url(r'^role/update/(?P<pk>\d+)$', views.RoleUpdate.as_view(), name = 'role-update'),
)