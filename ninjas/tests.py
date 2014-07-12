from django.test import TestCase
from django.utils import unittest
from ninjas.models import Ninja, Parent
from kanri import knowledge

class NinjaTestCase(TestCase):
	def setUp(self):
		self.p1 = Parent(
			name = 'John Smith',
			email = 'john@parent.com',
			phone = 0400000000
		)
		self.p1.save()

		self.p2 = Parent(
			name = 'Jane Smith',
			email = 'jane@parent.com',
			phone = 0400000001
		)
		self.p2.save()

		self.n1 = Ninja(
			name = 'Ninja One',
			email = 'one@ninja.com',
			gender = Ninja.MALE,
			postcode = 6000,
			school = 'Example Primary School',
			school_year = 4,
			allergies = 'Bullshit',
			attended_workshop = True,
			referral = '4chan',
			laptop = True,
			aim = "To hack the gibson",
			general_knowledge = knowledge.NOTHING,
			scratch_knowledge = knowledge.NOTHING,
			codecademy_knowledge = knowledge.NOTHING,
			language_experience = 'Brainfsck',
			black_belt = True,
			photo_release = True,
			parent = self.p1
		)

		self.n1.save()

	def test_get_short_name(self):
		self.assertEqual(self.n1.get_short_name(), 'Ninja O')