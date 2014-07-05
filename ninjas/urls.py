from django.conf.urls import patterns, url
from ninjas import views

urlpatterns = patterns('',
	url(r'^$',
		views.index,
		name = 'index'
	),
	
    url(r'^list$',
    	views.NinjaList.as_view(),
    	name = 'list'
    ),

    url(r'^(?P<pk>\d+)$',
    	views.NinjaDetail.as_view(),
    	name = 'detail'
    ),

    url(r'^add$',
    	views.NinjaCreate.as_view(),
    	name = 'add'
    ),

    url(r'^update/(?P<pk>\d+)$',
    	views.NinjaUpdate.as_view(),
    	name = 'update'
    ),

    url(r'^upload$',
    	views.upload,
    	name = 'upload'
    ),
)