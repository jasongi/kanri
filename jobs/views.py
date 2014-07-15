from django.shortcuts import render, get_object_or_404, redirect
from jobs.models import *
from jobs.forms import *
from mentors.models import *
from planner.models import DojoSession
from django.core.urlresolvers import reverse_lazy
from kanri.views import *
from django.http import Http404


# Job #
class JobCreate(KanriCreateView):
	model = Job

class JobList(KanriListView):
	model = Job
	template_name = 'jobs/index.html'

	def get_context_data(self, **kwargs):
		context = super(JobList, self).get_context_data(**kwargs)
		m = Mentor.objects.filter(user = self.request.user)
		if m:
			context['mentor'] = m[0]
		return context

class JobDetail(KanriDetailView):
	model = Job
	template_name = 'jobs/detail.html'

class JobUpdate(KanriUpdateView):
	model = Job

class JobDelete(KanriDeleteView):
	model = Job
	success_url = reverse_lazy('jobs:index')

def register(request, pk):
	job = get_object_or_404(Job, pk = pk)
	mentor = get_object_or_404(Mentor, user = request.user)

	if request.method == 'POST':
		mentor.jobs_desired.add(job)
		mentor.save()

	return redirect('jobs:index')

def unregister(request, pk):
	job = get_object_or_404(Job, pk = pk)
	mentor = get_object_or_404(Mentor, user = request.user)

	if request.method == 'POST':
		mentor.jobs_desired.remove(job)
		mentor.save()

	return redirect('jobs:index')


# Job Allocation #
def allocate_job(request, session_id, job_id):
	session = get_object_or_404(DojoSession, pk = session_id)
	job = get_object_or_404(Job, pk = job_id)

	if request.method == 'POST':
		form = JobAllocationForm(request.POST, session = session, job = job)

		if form.is_valid():
			for mentor in form.cleaned_data['mentors']:
				j = JobAllocation(
					job = job,
					session = session,
					mentor = mentor
				)

				j.save()

			return redirect('planner:roster', session.term.id)
	else:
		form = JobAllocationForm(session = session, job = job)

	return render(request, 'jobs/allocate.html', {
		'session': session,
		'job': job,
		'form': form,
	})

class JobAllocationDelete(KanriDeleteView):
	model = JobAllocation
	success_url = reverse_lazy('jobs:index')