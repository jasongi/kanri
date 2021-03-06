from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from planner import views

urlpatterns = patterns('',
    url(r'^$',
        views.index,
        name = 'index'
    ),

    url(r'^terms/add$',
        permission_required('planner.add_dojoterm')
        (views.add_term),
        name = 'terms-add'
    ),

    url(r'^terms$',
        permission_required('planner.read_dojoterm')
        (views.DojoTermList.as_view()),
        name = 'terms'
    ),

    url(r'^terms/(?P<pk>\d+)$',
        permission_required('planner.read_dojoterm')
        (views.DojoTermDetail.as_view()),
        name = 'terms-detail'
    ),

    url(r'^sessions/(?P<pk>\d+)$',
        permission_required('planner.read_dojosession')
        (views.DojoSessionDetail.as_view()),
        name = 'sessions-detail'
    ),

    url(r'^sessions/delete/(?P<pk>\d+)$',
        permission_required('planner.delete_dojosession')
        (views.DojoSessionDelete.as_view()),
        name = 'sessions-delete'
    ),

    url(r'^terms/delete/(?P<pk>\d+)$',
        permission_required('planner.delete_dojoterm')
        (views.DojoTermDelete.as_view()),
        name = 'terms-delete'
    ),



    url(r'^roster/allocate/(?P<session_id>\d+)/(?P<role_id>\d+)$',
        permission_required('planner.add_shift')
        (views.allocate),
        name = 'allocate'
    ),

    url(r'^roster/(?P<term_id>\d+)$',
        permission_required('planner.read_shift')
        (views.roster),
        name = 'roster'
    ),



    url(r'^shifts/(?P<pk>\d+)$',
        permission_required('planner.read_shift')
        (views.ShiftDetail.as_view()),
        name = 'shifts-detail'
    ),

    url(r'^shifts/delete/(?P<pk>\d+)$',
        permission_required('planner.delete_shift')
        (views.ShiftDelete.as_view()),
        name = 'shifts-delete'
    ),



    url(r'^rooms/add$',
        permission_required('planner.add_room')
        (views.RoomCreate.as_view()),
        name = 'rooms-add',
    ),

    url(r'^rooms$',
        permission_required('planner.read_room')
        (views.RoomList.as_view()),
        name = 'rooms-list',
    ),

    url(r'^rooms/(?P<pk>\d+)$',
        permission_required('planner.read_room')
        (views.RoomDetail.as_view()),
        name = 'rooms-detail'
    ),

    url(r'^rooms/update/(?P<pk>\d+)$',
        permission_required('planner.update_room')
        (views.RoomUpdate.as_view()),
        name = 'rooms-update'
    ),

    url(r'^rooms/delete/(?P<pk>\d+)$',
        permission_required('planner.delete_room')
        (views.RoomDelete.as_view()),
        name = 'rooms-delete'
    ),
)