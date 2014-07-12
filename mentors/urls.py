from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from mentors import views

urlpatterns = patterns('',
   url(r'^add$',
        permission_required('mentors.add_mentor')
        (views.MentorCreate.as_view()),
        name = 'add'
    ),

    url(r'^upload$',
        permission_required('mentors.add_mentor')
        (views.upload),
        name = 'upload'
    ),

    url(r'^$',
        permission_required('mentors.read_mentor')
        (views.MentorList.as_view()),
        name = 'index'
    ),

    url(r'^(?P<pk>\d+)$',
        permission_required('mentors.read_mentor')
        (views.MentorDetail.as_view()),
        name = 'detail'
    ),
    
    url(r'^update/(?P<pk>\d+)$',
        permission_required('mentors.update_mentor')
        (views.MentorUpdate.as_view()),
        name = 'update'
    ),
    
    url(r'^delete/(?P<pk>\d+)$',
        permission_required('mentors.delete_mentor')
        (views.MentorDelete.as_view()),
        name = 'delete'
    ),



    url(r'^role/add$',
        permission_required('mentors.add_role')
        (views.RoleCreate.as_view()),
        name = 'role-add'
    ),

    url(r'^role$',
        permission_required('mentors.read_role')
        (views.RoleList.as_view()),
        name = 'role-index'
    ),
    
    url(r'^role/(?P<pk>\d+)$',
        permission_required('mentors.read_role')
        (views.RoleDetail.as_view()),
        name = 'role-detail'
    ),
    
    url(r'^role/update/(?P<pk>\d+)$',
        permission_required('mentors.update_role')
        (views.RoleUpdate.as_view()),
        name = 'role-update'
    ),

    url(r'^delete/(?P<pk>\d+)$',
        permission_required('mentors.delete_role')
        (views.RoleDelete.as_view()),
        name = 'role-delete'
    ),
)