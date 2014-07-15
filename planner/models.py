from __future__ import division
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse, reverse_lazy
from ninjas.models import Ninja
from attendance.models import Attendance
from jobs.models import *
import datetime

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
        return reverse_lazy('planner:terms-detail', current_app = 'planner', args = [self.id])

    def __unicode__(self):
        return self.name

    class Meta():
        permissions = {
            ('read_dojoterm', "Can view a DojoTerm entry"),
        }

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
        return DojoSession.objects.filter(rooms = self)

    def get_absolute_url(self):
        return reverse_lazy('planner:rooms-detail', args = [self.id], current_app = 'planner')

    def __unicode__(self):
        return self.name

    class Meta():
        permissions = {
            ('read_room', "Can view a Room entry"),
        }



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
        mentoring = self.get_shifts().exclude(room = None)
        if mentoring.count() == 0:
            return None
        else:
            return round(self.ninja_set.count() / mentoring.count(), 2)

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
        s = Shift.objects.filter(session = self)
        return s

    def get_shifts_for_room(self, room):
        s = Shift.objects.filter(session = self, room = room)
        return s

    def get_shifts_per_room(self):
        l = []

        # Get global shifts.
        l.append({
            'room': None,
            'shifts': self.get_shifts_for_room(None)
        })

        # Get roomed shifts
        rooms = Room.objects.all()
        for room in rooms:
            room_details = {
                'room': room,
                'shifts': self.get_shifts_for_room(room)
            }
            l.append(room_details)
        return l
    
    def get_duration(self):
        return datetime.datetime.combine(datetime.datetime.now(), self.end) - datetime.datetime.combine(datetime.datetime.now(), self.start)

    def get_jobs_by_time(self):
        t = []
        for time in Job.TIME_CHOICES:
            jobs = JobAllocation.objects.filter(
                session = self,
                job__time = time[0]
            )

            t.append({
                'time': time[1],
                'job_allocations': jobs
            })

        print t
        return t



    def get_absolute_url(self):
        return reverse_lazy('planner:sessions-detail', current_app = 'planner', args = [self.id])

    def get_short_name(self):
        return self.date.strftime("%d/%m")

    def __unicode__(self):
        return "%s (%s)" % (self.get_short_name(), self.term)

    class Meta():
        permissions = {
            ('read_dojosession', "Can view a DojoSession entry"),
        }

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
        null = True,
        help_text = "The room, if any, that the mentor will be undertaking the shift in."
    )

    start = models.TimeField(
        blank = False,
        help_text = "Start Time"
    )

    end = models.TimeField(
        blank = False,
        help_text = "End Time"
    )

    def get_duration(self):
        return datetime.datetime.combine(datetime.datetime.now(), self.end) - datetime.datetime.combine(datetime.datetime.now(), self.start)

    def get_absolute_url(self):
        return reverse_lazy('planner:shifts-detail', current_app = 'planner', args = [self.id])

    def roster_name(self):
        return "%s (%s)" % (self.mentor, self.role.short_name)

    def __unicode__(self):
        return "%s (%s) for %s" % (self.mentor, self.role, self.session)

    class Meta():
        permissions = {
            ('read_shift', "Can view a Shift entry"),
        }
