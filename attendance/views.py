from django.shortcuts import render, get_object_or_404, redirect
from planner.models import DojoSession, DojoTerm
from ninjas.models import Ninja
from attendance.models import Attendance
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime

def index(request):
	sessions = DojoSession.objects.filter(date__gt = timezone.now()).order_by('date')[:5]
	return render(request, 'attendance/index.html', {
		'sessions': sessions,
		})

def signoff(request, dojo_session_id):
	session = DojoSession.objects.get(pk = dojo_session_id)
	ninja_vm = []

	for ninja in Ninja.objects.all():
		here = Attendance.objects.filter(ninja = ninja, session = session)
		if here:
			here = here[0]

		ninja_vm.append({
			'ninja': ninja,
			'attending': session in ninja.availabilities.all(),
			'here': here
		})

	return render(request, 'attendance/signoff.html', {
		'session': session,
		'object_list': ninja_vm,
		'ninja_count': len(ninja_vm),
		'expected_attendance': session.get_expected_attendance(),
		'expected_attendance_percentage': session.get_expected_attendance_percentage(),
		'attendance': session.get_attendance(),
		'attendance_percentage': session.get_attendance_percentage(),
		'attendance_gap': session.get_expected_attendance_percentage() - session.get_attendance_percentage(),
	})

def here(request, session_id, ninja_id):
	if request.method == "POST":
		ninja = get_object_or_404(Ninja, pk = ninja_id)
		print session_id
		session = get_object_or_404(DojoSession, pk = session_id)

		a = Attendance(
			ninja = ninja,
			session = session,
			added_by = request.user
		)

		a.save()

	return redirect('attendance:signoff', dojo_session_id = session_id)

def nothere(request, attendance_id):
	if request.method == "POST":
		attendance = get_object_or_404(Attendance, pk = attendance_id)
		session_id = attendance.session_id
		attendance.delete()

		return redirect('attendance:signoff', dojo_session_id = session_id)

	