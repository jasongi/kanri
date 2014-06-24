from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'osameru.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mentors/', include('mentors.urls', namespace = "mentors")),
    url(r'^ninjas/', include('ninjas.urls', namespace = "ninjas")),
    url(r'^planner/', include('planner.urls', namespace = "planner")),
    url(r'^attendance/', include('attendance.urls', namespace = "attendance")),
)
