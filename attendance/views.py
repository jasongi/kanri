from django.shortcuts import render, get_object_or_404
from planner.models import DojoSession, DojoTerm
import django.utils.timezone
import datetime

def index(request):
	sessions = DojoSession.objects.all().order_by('date_time_start')[:5]
	return render(request, 'attendance/index.html', {
		'sessions': sessions,
		})

def signoff(request, dojo_session_id):
	dojo = DojoSession.objects.get(pk = dojo_session_id)
	return render(request, 'attendance/signoff.html', {
		'dojo': dojo
		})