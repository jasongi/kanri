from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name = 'index'),
    url(r'^login/?$',
    	views.login,
    	name = 'login'
    ),
    
    url(r'^logout?/$',
    	views.logout,
    	name = 'logout'
    ),
    

    url(r'^permissions$',
    	views.permissions,
    	name = 'permissions'
    ),

    url(r'^permissions/sync$',
    	views.sync,
    	name = 'permissions-sync'
    ),

    url(r'^permissions/management/add$',
    	views.management_add,
    	name = 'management-add',
    ),

    url(r'^permissions/management/remove$',
    	views.management_remove,
    	name = 'management-remove',
    ),

    url(r'^cp$',
    	views.cp,
    	name = 'cp'
    ),
)