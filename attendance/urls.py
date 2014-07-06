from django.conf.urls import patterns, url

from attendance import views

urlpatterns = patterns('',
    url(r'^$',
    	views.index,
    	name = 'index'
    ),

    url(r'^signoff/(?P<dojo_session_id>\d+)$',
    	views.signoff,
    	name = 'signoff'
    ),

    url(r'^signoff/here/(?P<session_id>\d+)/(?P<ninja_id>\d+)',
    	views.here,
    	name = 'here'
    ),

    url(r'^signoff/nothere/(?P<attendance_id>\d+)',
    	views.nothere,
    	name = 'nothere'
    )
)