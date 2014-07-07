from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from attendance import views

urlpatterns = patterns('',
    url(r'^$',
    	views.index,
    	name = 'index'
    ),

    url(r'^signoff/(?P<dojo_session_id>\d+)$',
        permission_required('attendance.view_attendance')
    	(views.signoff),
    	name = 'signoff'
    ),

    url(r'^signoff/here/(?P<session_id>\d+)/(?P<ninja_id>\d+)',
        permission_required('attendance.add_attendance')
    	(views.here),
    	name = 'here'
    ),

    url(r'^signoff/nothere/(?P<attendance_id>\d+)',
        permission_required('attendance.delete_attendance')
    	(views.nothere),
    	name = 'nothere'
    )
)