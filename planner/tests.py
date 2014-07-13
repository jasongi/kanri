from django.test import TestCase
from django.utils import unittest
from planner.models import *
from kanri import knowledge
import datetime

class PlannerTestCase(TestCase):
    def setUp(self):
        # Create Term
        self.t = DojoTerm(
            name = "Example Term"
        )

        self.t.save()

        # Create Rooms
        for i in range(1, 17):
            r = Room(
                name = "Room %s" % i,
                capacity = 10 * i
            )

            r.save()

        # Create Sessions
        starting_dt = datetime.date(2001, 04, 20)
        start_time = datetime.time(04, 20)
        end_time = datetime.time(16, 20)
        week_delta = datetime.timedelta(days = 7)

        current_dt = starting_dt

        self.sessions = []
        for i in range(1, 9):
            s = DojoSession(
                term = self.t,
                date = current_dt,
                start = start_time,
                end = end_time,
            )

            s.save()

            # There are 16 rooms and 8 sessions. To allocate a different room to
            # each session (makes testing better) we just use the PK of the session
            # to choose the first room. To choose a second room we use the PK and
            # multiply it by 2.
            s.rooms.add(Room.objects.get(pk = s.id))
            s.rooms.add(Room.objects.get(pk = s.id * 2))
            s.save()

            self.sessions.append(s)

            current_dt += week_delta
        
    def test_get_session_count(self):
        self.assertEqual(self.t.get_session_count(), 8)

    def test_get_sessions(self):
        # Check length is the same.
        self.assertEqual(len(self.t.get_sessions()), 8)

        # Check that it only contains sessions that we made earlier.
        for session in self.t.get_sessions():
            self.assertIn(session, self.sessions)

    def test_get_first_session(self):
        self.assertEqual(self.t.get_first_session(), self.sessions[0])

    def test_get_last_session(self):
        self.assertEqual(self.t.get_last_session(), self.sessions[-1])

    ## DojoSession Test ##
    def test_get_capacity(self):
        # Test the capacity of each session based on the rooms we allocated earlier.
        # The capacity is calculated on-the-fly based on the way room capacities are
        # allocated and calculated in setUp()
        for session in self.sessions:
            capacity = (10 * session.id) + (session.id * 2 * 10)
            self.assertEqual(session.get_capacity(), capacity) 

    def test_get_duration(self):
        # This can be done a lot better by allocating different deterministic
        # dates to each session.
        self.assertEqual(self.sessions[0].get_duration(), datetime.timedelta(hours = 12))
