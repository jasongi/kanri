from django.shortcuts import render
from planner.models import DojoTerm, DojoSession
from planner.forms import DojoTermForm
from kanri.views import *
from django.utils import timezone
from django.shortcuts import redirect
import datetime
import time

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

			curr_date = first_date
			week_td = datetime.timedelta(days = 7)

			for week in range(form.cleaned_data['weeks']):
				print "Week %s: %s from %s to %s" % (week + 1, curr_date, start, end)
				s = DojoSession(term = t, date = curr_date, start = start, end = end)
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

class DojoSessionCreate(KanriCreateView):
	model = DojoSession

class DojoSessionDetail(KanriDetailView):
	model = DojoSession
	template_name = 'planner/session/detail.html'