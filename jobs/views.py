from django.shortcuts import render, get_object_or_404, redirect
from jobs.models import *
from jobs.forms import *
from planner.models import DojoSession
from django.core.urlresolvers import reverse_lazy
from kanri.views import *

# Job #
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