from django.shortcuts import render, get_object_or_404
from planner.models import *
from planner.forms import *
from mentors.models import Role
from kanri.views import *
from django.utils import timezone
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.forms.formsets import formset_factory
import datetime
import time

def index(request):
	return render(request, 'planner/index.html')

## Term ##
def add_term(request):
	if request.method == "POST":
		form = DojoTermForm(request.POST)
		if form.is_valid():
			# Create Term
			t = DojoTerm(name = form.cleaned_data['name'])
			t.save()

			# Create sessions for term.
			first_date = form.cleaned_data['first_session_date']
			start = form.cleaned_data['first_session_start']
			end = form.cleaned_data['first_session_end']
			rooms = form.cleaned_data['rooms']

			curr_date = first_date
			week_td = datetime.timedelta(days = 7)

			for week in range(form.cleaned_data['weeks']):
				s = DojoSession(
					term = t,
					date = curr_date,
					start = start,
					end = end,
				)

				s.save()

				for room in rooms:
					s.rooms.add(room)

				s.save()

				curr_date += week_td

			# We're done here.
			return redirect(t)

	else:
		form = DojoTermForm()

	return render(request, 'planner/term/add.html', {
		'form': form,
	})

class DojoTermList(KanriListView):
	model = DojoTerm
	template_name = 'planner/term/list.html'

class DojoTermDetail(KanriDetailView):
	model = DojoTerm
	template_name = 'planner/term/detail.html'

class DojoTermDelete(KanriDeleteView):
	model = DojoTerm
	success_url = reverse_lazy('planner:terms', current_app = 'planner')

## Shifts ##
def allocate(request, session_id, role_id):
	session = get_object_or_404(DojoSession, pk = session_id)
	role = get_object_or_404(Role, pk = role_id)

	if request.method == 'POST':
		form = ShiftAllocationForm(request.POST, session = session, role = role)

		if form.is_valid():
			s = Shift(
				mentor = form.cleaned_data['mentor'],
				session = session,
				role = role,
				room = form.cleaned_data['room'],
				start = form.cleaned_data['start'],
				end = form.cleaned_data['end']
			)
			
			s.save()
			return redirect('planner:roster', session.term.id)
	else:
		form = ShiftAllocationForm(session = session, role = role)

	return render(request, 'planner/allocate.html', {
		'session': session,
		'role': role,
		'form': form,
	})


def roster(request, term_id):
	term = DojoTerm.objects.get(pk = term_id)
	sessions = DojoSession.objects.filter(term = term)
	roles = Role.objects.all()
	jobs = Job.objects.all

	return render(request, 'planner/roster.html', {
		'term': term,
		'sessions': sessions,
		'roles': roles,
		'jobs': jobs,
	})

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

	return render(request, 'planner/job/allocate.html', {
		'session': session,
		'job': job,
		'form': form,
	})

class ShiftDetail(KanriDetailView):
	model = Shift
	template_name = 'planner/shift/detail.html'

class ShiftDelete(KanriDeleteView):
	model = Shift
	success_url = reverse_lazy('planner:terms')



## Dojo Sessions ##
class DojoSessionDetail(KanriDetailView):
	model = DojoSession
	template_name = 'planner/session/detail.html'

	def get_context_data(self, **kwargs):
		context = super(DojoSessionDetail, self).get_context_data(**kwargs)
		context['roles'] = Role.objects.order_by('name')
		return context

class DojoSessionDelete(KanriDeleteView):
	model = DojoSession
	success_url = reverse_lazy('planner:terms')

## Room ##
class RoomCreate(KanriCreateView):
	model = Room

class RoomDetail(KanriDetailView):
	model = Room
	template_name = 'planner/room/detail.html'

class RoomList(KanriListView):
	model = Room
	template_name = 'planner/room/list.html'

class RoomUpdate(KanriUpdateView):
	model = Room

class RoomDelete(KanriDeleteView):
	model = Room
	success_url = reverse_lazy('planner:rooms-list')