from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from ninjas import views

urlpatterns = patterns('',
	url(r'^$',
        permission_required('ninjas.view_ninja')
		(views.index),
		name = 'index'
	),
	
    url(r'^list$',
        permission_required('ninjas.view_ninja')
    	(views.NinjaList.as_view()),
    	name = 'list'
    ),

    url(r'^(?P<pk>\d+)$',
        permission_required('ninjas.view_ninja')
    	(views.NinjaDetail.as_view()),
    	name = 'detail'
    ),

    url(r'^add$',
        permission_required('ninjas.add_ninja')
    	(views.NinjaCreate.as_view()),
    	name = 'add'
    ),

    url(r'^update/(?P<pk>\d+)$',
        permission_required('ninjas.upload_ninja')
    	(views.NinjaUpdate.as_view()),
    	name = 'update'
    ),

    url(r'^upload$',
        permission_required('ninjas.add_ninja')
    	(views.upload),
    	name = 'upload'
    ),
)