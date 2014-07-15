from django.shortcuts import render, get_object_or_404
from jobs.models import Job
from django.core.urlresolvers import reverse_lazy
from kanri.views import *

class JobCreate(KanriCreateView):
	model = Job

class JobList(KanriListView):
	model = Job
	template_name = 'jobs/index.html'

class JobDetail(KanriDetailView):
	model = Job
	template_name = 'jobs/detail.html'

class JobUpdate(KanriUpdateView):
	model = Job

class JobDelete(KanriDeleteView):
	model = Job
	success_url = reverse_lazy('jobs:index')