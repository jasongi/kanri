from django.conf.urls import patterns, url

from mentors import views

urlpatterns = patterns('',
    url(r'^$', views.MentorList.as_view(), name = 'index'),
    url(r'^(?P<pk>\d+)$', views.MentorDetail.as_view(), name = 'detail'),
    url(r'^add$', views.MentorCreate.as_view(), name = 'add'),
    url(r'^update/(?P<pk>\d+)$', views.MentorUpdate.as_view(), name = 'update'),
    url(r'^upload$', views.upload, name = 'upload'),
    url(r'^role$', views.RoleList.as_view(), name = 'role-index'),
    url(r'^role/(?P<pk>\d+)$', views.RoleDetail.as_view(), name = 'role-detail'),
    url(r'^role/add$', views.RoleCreate.as_view(), name = 'role-add'),
    url(r'^role/update/(?P<pk>\d+)$', views.RoleUpdate.as_view(), name = 'role-update'),
)