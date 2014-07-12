from django.test import TestCase
from django.utils import unittest
from mentors.models import Mentor
from accounts.models import KanriUser, KanriUserManager
from kanri import knowledge

class NinjaTestCase(TestCase):
	def setUp(self):
		self.u1 = KanriUser.objects.create_user(
			email = 'mail@example.com',
			first_name = 'John',
			last_name = 'Smith',
			password = 'useless420',
		)

		self.u1.phone_number = '0400000000'

		self.u1.save()

		self.m1 = Mentor(
			uni = 'Notre Dame',
			uni_study = 'Basket Weaving',
			work = 'CEO',
			shirt_size = Mentor.FEMALE_EXTRA_LARGE,
			needs_shirt = True,
			curtin_status = Mentor.NEITHER,
			coding_experience = knowledge.NOTHING,
			children_experience = knowledge.NOTHING,
			user = self.u1
		)
		self.m1.save()

	def test_name(self):
		self.assertEqual(self.m1.name(), 'John S')

	def test_get_call_url(self):
		self.assertEqual(self.m1.get_call_url(), 'tel:0400000000')

	def test_get_email_url(self):
		self.assertEqual(self.m1.get_email_url(), 'mailto:mail@example.com')

	def test_wwcc_status_correct(self):
		# Just WWCC number
		self.m1.wwcc = 1234
		self.assertEqual(self.m1.get_wwcc_status(), 'Recorded (1234)')
		
		# Just WWCC receipt
		self.m1.wwcc = None
		self.m1.wwcc_receipt = 5678
		self.assertEqual(self.m1.get_wwcc_status(), 'Processing (5678)')

		# Number and receipt
		self.m1.wwcc = 1234
		self.m1.wwcc_receipt = 5678
		self.assertEqual(self.m1.get_wwcc_status(), 'Recorded (1234)')

	def test_get_curtin_status_correct(self):
		# Neither
		self.assertEqual(self.m1.get_curtin_status(), 'Neither/not sure')

		# Staff (No ID)
		self.m1.curtin_status = Mentor.STAFF
		self.assertEqual(self.m1.get_curtin_status(), 'Staff')

		# Associate (No ID)
		self.m1.curtin_status = Mentor.ASSOCIATE
		self.assertEqual(self.m1.get_curtin_status(), 'Associate')

		# Associate (ID)
		self.m1.curtin_id = '123456J'
		self.assertEqual(self.m1.get_curtin_status(), 'Associate (123456J)')

		# Staff (ID)
		self.m1.curtin_status = Mentor.STAFF
		self.assertEqual(self.m1.get_curtin_status(), 'Staff (123456J)')

