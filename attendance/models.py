from django.db import models
from ninjas.models import Ninja
from planner.models import DojoSession, DojoTerm
from django.contrib.auth.models import User
from django.conf import settings

class Attendance(models.Model):
	ninja = models.ManyToManyField(Ninja)
	dojo = models.ForeignKey(DojoSession)
	time = models.DateTimeField(auto_now_add = True)
	added_by = models.OneToOneField(settings.AUTH_USER_MODEL, unique = True)