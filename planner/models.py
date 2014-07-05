from django.db import models
from django.utils import timezone
from ninjas.models import Ninja

class DojoTerm(models.Model):
	name = models.CharField(max_length = 50, blank = False)

	def get_sessions(self):
		return DojoSession.objects.filter(term = self).count()

	def get_ninjas(self):
		return Ninja.objects.filter(availabilities__term = self).count()

	def __unicode__(self):
		return self.name

class DojoSession(models.Model):
	term = models.ForeignKey(DojoTerm, help_text = "Dojo Term")
	date_time_start = models.DateTimeField(unique = True, help_text = "Start Time")
	date_time_end = models.DateTimeField(unique = True, help_text = "End Time")

	def coming_up(self):
		return abs((self.date_time_start - timezone.now).total_seconds()) < (2 * 60 * 60) # 2 hours

	def __unicode__(self):
		return "Session for %s (%s from %s to %s)" % (self.term,
			self.date_time_start.strftime("%d/%m/%y"), 
			self.date_time_start.strftime("%I:%M %p"),
			self.date_time_end.strftime("%I:%M %p"),
		)