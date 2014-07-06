from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from ninjas.models import Ninja

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
		return self.ninja_set.count() / self.mentor_set.count()

	def get_absolute_url(self):
		return reverse('planner:sessions-detail', current_app = 'planner', args = [self.id])

	def __unicode__(self):
		return "%s (%s)" % (self.date.strftime("%d/%m"), self.term)