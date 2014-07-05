from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

from planner import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name = 'index'),
    url(r'^terms$',
    	permission_required('planner.view_dojoterm')
    	(views.DojoTermList.as_view()),
    	name = 'terms'
    ),

    url(r'^terms/(?P<pk>\d+)$',
        permission_required('planner.view_dojoterm')
        (views.DojoTermDetail.as_view()),
        name = 'term-detail'
    ),

    url(r'^terms/add$',
    	permission_required('planner.add_dojoterm')
    	(views.add_term),
    	name = 'terms-add'
    ),

    url(r'^sessions/(?P<pk>\d+)$',
        permission_required('planner.view_dojosession')
        (views.DojoSessionDetail.as_view()),
        name = 'session-detail'
    ),

    url(r'^sessions/add$',
        permission_required('planner.add_dojosession')
        (views.DojoSessionCreate.as_view()),
        name = 'sessions'
    ),
)