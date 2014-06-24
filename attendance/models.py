from django.db import models
from ninjas.models import Ninja
from planner.models import DojoSession, DojoTerm
from django.contrib.auth.models import User

class Attendance(models.Model):
	ninja = models.ManyToManyField(Ninja)
	dojo = models.ForeignKey(DojoSession)
	time = models.DateTimeField(auto_now_add = True)
	added_by = models.OneToOneField(User, unique = True)