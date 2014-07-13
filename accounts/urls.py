from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name = 'index'),
    url(r'^login/?$',
    	views.login,
    	name = 'login'
    ),
    
    url(r'^logout/?$',
    	views.logout,
    	name = 'logout'
    ),
    

    url(r'^admin$',
    	views.admin,
    	name = 'admin'
    ),

    url(r'^admin/pass$',
        views.change_password_admin,
        name = 'admin-password'
    ),

    url(r'^admin/sync$',
    	views.sync,
    	name = 'permissions-sync'
    ),

    url(r'^admin/management/add$',
    	views.management_add,
    	name = 'management-add',
    ),

    url(r'^admin/management/remove$',
    	views.management_remove,
    	name = 'management-remove',
    ),

    url(r'^cp$',
    	views.cp,
    	name = 'cp'
    ),
)