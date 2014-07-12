from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Attendance(models.Model):
    ninja = models.ForeignKey('ninjas.Ninja')
    session = models.ForeignKey('planner.DojoSession')
    time = models.DateTimeField(auto_now_add = True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    class Meta():
        permissions = {
            ('read_attendance', "Can view an Attendance entry"),
        }