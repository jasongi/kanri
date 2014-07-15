from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required, permission_required
from jobs import views

urlpatterns = patterns('',
    # job
    url(r'^add$',
        permission_required('jobs.add_job')
        (views.JobCreate.as_view()),
        name = 'add'
    ),

    url(r'^$',
        permission_required('jobs.read_job')
        (views.JobList.as_view()),
        name = 'index'
    ),

    url(r'^(?P<pk>\d+)$',
        permission_required('jobs.read_job')
        (views.JobDetail.as_view()),
        name = 'detail'
    ),

    url(r'^update/(?P<pk>\d+)$',
        permission_required('jobs.change_job')
        (views.JobUpdate.as_view()),
        name = 'update'
    ),

    url(r'^delete/(?P<pk>\d+)$',
        permission_required('jobs.delete_job')
        (views.JobDelete.as_view()),
        name = 'delete'
    ),

    # Job Allocation
    url(r'^allocate/(?P<session_id>\d+)/(?P<job_id>\d+)$',
        permission_required('job.add_joballocation')
        (views.allocate_job),
        name = 'allocate'
    ),

    url(r'^delete/allocation/(?P<pk>\d+)$',
        permission_required('jobs.delete_joballocation')
        (views.JobAllocationDelete.as_view()),
        name = 'allocate-delete'
    ),

    # Job Registration
    url(r'^register/(?P<pk>\d+)$',
        permission_required('job.register_for_job')
        (views.register),
        name = 'register'
    ),

    url(r'^unregister/(?P<pk>\d+)$',
        permission_required('job.register_for_job')
        (views.unregister),
        name = 'unregister'
    ),
)