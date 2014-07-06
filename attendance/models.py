from django.db import models
from ninjas.models import Ninja
from django.contrib.auth.models import User
from django.conf import settings

class Attendance(models.Model):
	ninja = models.ForeignKey(Ninja)
	session = models.ForeignKey('planner.DojoSession')
	time = models.DateTimeField(auto_now_add = True)
	added_by = models.ForeignKey(settings.AUTH_USER_MODEL)