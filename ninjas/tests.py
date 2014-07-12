from django.test import TestCase
from django.utils import unittest
from ninjas.models import Ninja, Parent
from kanri import knowledge

class NinjaTestCase(TestCase):
	def setUp(self):
		self.p1 = Parent(
			name = 'John Smith',
			email = 'john@parent.com',
			phone = '0400000000'
		)
		self.p1.save()

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

		self.n2 = Ninja(
			name = 'Ninja Two',
			email = 'two@ninja.com',
			gender = Ninja.FEMALE,
			postcode = 6000,
			school = 'Example Primary School',
			school_year = 4,
			attended_workshop = False,
			referral = '4chan',
			laptop = True,
			aim = "To hack the gibson",
			general_knowledge = knowledge.NOTHING,
			scratch_knowledge = knowledge.NOTHING,
			codecademy_knowledge = knowledge.NOTHING,
			language_experience = 'Brainfsck',
			black_belt = False,
			photo_release = False,
			parent = self.p1
		)
		self.n2.save()

	def test_get_short_name(self):
		self.assertEqual(self.n1.get_short_name(), 'Ninja O')

	def test_get_call_url(self):
		self.assertEqual(self.n1.get_call_url(), 'tel:0400000000')

	def test_get_email_url(self):
		self.assertEqual(self.n1.get_email_url(), 'mailto:john@parent.com')

	def test_parent_required_lower(self):
		self.n1.school_year = 5
		self.n1.save()
		self.assertTrue(self.n1.parent_required())

	def test_parent_required_border(self):
		self.n1.school_year = 6
		self.n1.save()
		self.assertTrue(self.n1.parent_required())

	def test_parent_required_higher(self):
		self.n1.school_year = 7
		self.n1.save()
		self.assertFalse(self.n1.parent_required())

	def test_get_new(self):
		self.assertEqual(Ninja.get_new(), 1)

	def test_get_returning(self):
		self.assertEqual(Ninja.get_returning(), 1)

	def test_get_allergies(self):
		a = Ninja.get_allergies()
		self.assertEqual(len(a), 1)
		self.assertEqual(a[0], self.n1)

	def test_get_photos(self):
		a = Ninja.get_photos()
		self.assertEqual(len(a), 1)
		self.assertEqual(a[0], self.n2)

	def test_get_male(self):
		self.assertEqual(Ninja.get_male(), 1)

	def test_get_female(self):
		self.assertEqual(Ninja.get_female(), 1)
