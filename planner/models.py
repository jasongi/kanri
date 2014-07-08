from __future__ import division
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from ninjas.models import Ninja
from attendance.models import Attendance

class DojoTerm(models.Model):
	name = models.CharField(max_length = 50, blank = False)

	def get_session_count(self):
		return DojoSession.objects.filter(term = self).count()

	def get_sessions(self):
		return DojoSession.objects.filter(term = self)

	def get_first_session(self):
		sessions = DojoSession.objects.filter(term = self).order_by('date')
		if sessions:
			return sessions[0]

	def get_last_session(self):
		sessions = DojoSession.objects.filter(term = self).order_by('-date')
		if sessions:
			return sessions[0]

	def get_ninjas(self):
		return Ninja.objects.filter(availabilities__term = self).distinct().count()
	
	def get_ratio(self):
		sessions = self.get_sessions()
		total = 0
		for session in sessions:
			total = total + session.get_ratio()
		total /= len(sessions)
		return round(total, 2)

	def get_absolute_url(self):
		return reverse('planner:terms-detail', current_app = 'planner', args = [self.id])

	def __unicode__(self):
		return self.name

class Room(models.Model):
	name = models.CharField(
		blank = False,
		unique = True,
		max_length = 50,
		help_text = 'The name of the room.'
	)

	capacity = models.PositiveIntegerField(
		blank = False,
		help_text = 'The number of ninjas that can fit into the room.'
	)

	def get_sessions(self):
		return DojoSession.objects.filter(room = self)
	def __unicode__(self):
		return self.name

class DojoSession(models.Model):
	term = models.ForeignKey(DojoTerm, help_text = "Dojo Term")
	date = models.DateField(
		blank = False,
		help_text = "Date during which the session will take place."
	)

	start = models.TimeField(
		blank = False,
		help_text = "Start Time"
	)

	end = models.TimeField(
		blank = False,
		help_text = "End Time"
	)

	rooms = models.ManyToManyField(
		Room,
		blank = True,
		help_text = "The rooms in which this session will be running."
	)

	def coming_up(self):
		return abs((self.date_time_start - timezone.now).total_seconds()) < (2 * 60 * 60) # 2 hours
	
	def get_ratio(self):
		if self.mentor_set.count() == 0:
			return None
		else:
			return self.ninja_set.count() / self.mentor_set.count()

	def get_capacity(self):
		capacity = 0
		for room in self.rooms.all():
			capacity += room.capacity
		return capacity

	def get_expected_attendance(self):
		return Ninja.objects.filter(availabilities = self).count()

	def get_expected_attendance_percentage(self):
		ninja_count = Ninja.objects.count()
		if ninja_count != 0:
			return (int)((self.get_expected_attendance() / ninja_count) * 100)
		else:
			return 0

	def get_attendance(self):
		return Attendance.objects.filter(session = self).count()

	def get_attendance_percentage(self):
		ninja_count = Ninja.objects.count()
		if ninja_count != 0:
			return (int)((self.get_attendance() / ninja_count) * 100)
		else:
			return 0

	def get_shifts(self):
		return Shift.objects.filter(session = self)

	def get_shifts_for_room(self, room):
		return self.get_shifts().filter(room)

	def get_absolute_url(self):
		return reverse('planner:sessions-detail', current_app = 'planner', args = [self.id])

	def get_short_name(self):
		return self.date.strftime("%d/%m")

	def __unicode__(self):
		return "%s (%s)" % (self.get_short_name(), self.term)

class Shift(models.Model):
	mentor = models.ForeignKey(
		'mentors.Mentor',
		blank = False,
		help_text = 'The mentor unergoing this shift.'
	)

	session = models.ForeignKey(
		DojoSession,
		blank = False,
		help_text = 'The session during which this shift takes place.',
	)

	role = models.ForeignKey(
		'mentors.Role',
		blank = False,
		help_text = "The role that the mentor will be undertaking during this shift.",
	)

	room = models.ForeignKey(
		Room,
		blank = True,
		help_text = "The room, if any, that the mentor will be undertaking the shift in."
	)