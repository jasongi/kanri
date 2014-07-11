from planner.forms import DojoTermForm
from django.shortcuts import render, get_object_or_404
from planner.models import DojoTerm, DojoSession, Room, Shift
from kanri.views import *
from django.utils import timezone
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
import datetime
import time

def index(request):
	return render(request, 'planner/index.html')

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

def roster(request, term_id):
	term = DojoTerm.objects.get(pk = term_id)
	sessions = DojoSession.objects.filter(term = term)

	# Get list of used rooms.
	# There's probably a distinct query I could use that'd be a lot cheaper.
	rooms = []
	for session in sessions:
		for room in session.rooms.all():
			if not room in rooms:
				rooms.append(room)

	roster = []
	for room in rooms:
		room_usage = []
		for session in sessions:
			room_usage.append(Shift.objects.filter(room = room, session = session))
		roster.append({
			'room': room,
			'usage': room_usage
		})

	return render(request, 'planner/roster.html', {
		'term': term,
		'sessions': sessions,
		'rooms': rooms,
		'roster': roster,
	})

def allocate(request, session_id, role_id):
	session = get_object_or_404(DojoSession, pk = session_id)
	role = get_object_or_404(Role, pk = session_id)

	form = ShiftAllocationForm(session = session, role = role)

	return render(request, 'planner/allocate.html', {
		'session': session,
		'role': role,
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

class ShiftDetail(KanriDetailView):
	model = Shift
	template_name = 'planner/shift/detail.html'

class ShiftDelete(KanriDeleteView):
	model = Shift
	success_url = reverse_lazy('planner:index')

class DojoSessionDetail(KanriDetailView):
	model = DojoSession
	template_name = 'planner/session/detail.html'



class RoomCreate(KanriCreateView):
	model = Room

class RoomDetail(KanriDetailView):
	model = Room
	template_name = 'planner/room/detail.html'

class RoomList(KanriListView):
	model = Room
	template_name = 'planner/room/list.html'