from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from ninjas import views

urlpatterns = patterns('',

   url(r'^add$',
        permission_required('ninjas.add_ninja')
        (views.NinjaCreate.as_view()),
        name = 'add'
    ),

    url(r'^upload$',
        permission_required('ninjas.add_ninja')
        (views.upload),
        name = 'upload'
    ),

	url(r'^$',
        permission_required('ninjas.read_ninja')
		(views.index),
		name = 'index'
	),
	
    url(r'^list$',
        permission_required('ninjas.read_ninja')
    	(views.NinjaList.as_view()),
    	name = 'list'
    ),

    url(r'^(?P<pk>\d+)$',
        permission_required('ninjas.read_ninja')
    	(views.NinjaDetail.as_view()),
    	name = 'detail'
    ),

    url(r'^update/(?P<pk>\d+)$',
        permission_required('ninjas.update_ninja')
    	(views.NinjaUpdate.as_view()),
    	name = 'update'
    ),

    url(r'^delete/(?P<pk>\d+)$',
        permission_required('ninjas.delete_ninja')
        (views.NinjaDelete.as_view()),
        name = 'delete'
    ),
)