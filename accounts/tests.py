from django.test import TestCase
from django.utils import unittest
from accounts.models import KanriUser, KanriUserManager
from django.contrib.auth import authenticate
# Create your tests here.
class AccountTestCase(TestCase):
	u1_email = 'user1@example.com'
	u1_first_name = "User",
	u1_last_name = "One",
	u1_password = 'PasswordForUser1'

	u2_email = 'user2@example.com'
	u2_first_name = "User",
	u2_last_name = "Two",
	u2_password = 'PasswordForUser2'

	def setUp(self):
		self.u1 = KanriUser.objects.create_user(
			email = self.u1_email,
			first_name = self.u1_first_name,
			last_name = self.u1_last_name,
			password = self.u1_password
		)
		self.u1.save()

		self.u2 = KanriUser.objects.create_superuser(
			email = self.u2_email,
			first_name = self.u2_first_name,
			last_name = self.u2_last_name,
			password = self.u2_password
		)
		self.u2.save

	def test_auth_with_correct_credetials(self):
		self.assertEqual(authenticate(username = self.u1_email, password = self.u1_password), self.u1)

	def test_auth_with_incorrect_credentials(self):
		self.assertEqual(authenticate(username = self.u1_email, password = self.u1_password + '1'), None)

	def test_superuser_auth_with_correct_credetials(self):
		self.assertEqual(authenticate(username = self.u2_email, password = self.u2_password), self.u2)

	def test_superuser_auth_with_incorrect_credentials(self):
		self.assertEqual(authenticate(username = self.u2_email, password = self.u2_password + '1'), None)