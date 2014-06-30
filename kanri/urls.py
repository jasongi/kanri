from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dashboard.views.index', name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ninjas/', include('ninjas.urls', namespace = "ninjas")),
    url(r'^planner/', include('planner.urls', namespace = "planner")),
    url(r'^attendance/', include('attendance.urls', namespace = "attendance")),
    url(r'^accounts/', include('accounts.urls', namespace = "accounts")),
    url(r'^mentors/', include('mentors.urls', namespace = "mentors")),
)
