from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required

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
        permission_required('accounts.see_admin')
    	(views.admin),
    	name = 'admin'
    ),

    url(r'^admin/pass$',
        permission_required('accounts.change_user_password')
        (views.change_password_admin),
        name = 'admin-password'
    ),

    url(r'^admin/sync$',
        permission_required('accounts.sync_permissions')
    	(views.sync),
    	name = 'permissions-sync'
    ),

    url(r'^admin/management/add$',
        permission_required('accounts.add_management')
    	(views.management_add),
    	name = 'management-add',
    ),

    url(r'^admin/management/remove$',
        permission_required('accounts.remove_management')
    	(views.management_remove),
    	name = 'management-remove',
    ),
)