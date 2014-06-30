from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
	"""A role somebody can take in a CoderDojo term."""
	name = models.CharField(max_length = 50, blank = False, help_text = "The name of the role.")
	short_name = models.CharField(max_length = 10, blank = False, help_text = "A short name for this role. Used in spreadsheets.")
	description = models.TextField(max_length = 1024, blank = False, help_text = "The role's long description.")

class Mentor(models.Model):
	MALE_SMALL = "MS"
	MALE_MEDIUM = "MM"
	MALE_LARGE = "ML"
	MALE_EXTRA_LARGE = "MXL"

	FEMALE_EXTRA_SMALL = "FXS"
	FEMALE_SMALL = "FS"
	FEMALE_MEDIUM = "FM"
	FEMALE_LARGE = "FL"
	FEMALE_EXTRA_LARGE = "FXL"

	SHIRT_SIZE_CHOICES = (
		('Male', (
			(MALE_SMALL, "Male S"),
			(MALE_MEDIUM, "Male M"),
			(MALE_LARGE, "Male L"),
			(MALE_EXTRA_LARGE, "Male XL")
		)),
		('Female', (
			(FEMALE_EXTRA_SMALL, "Female XS"),
			(FEMALE_SMALL, "Female S"),
			(FEMALE_MEDIUM, "Female M"),
			(FEMALE_LARGE, "Female L"),
			(FEMALE_EXTRA_LARGE, "Female XL")
		))
	)

	ASSOCIATE = 'A'
	STAFF = 'S'
	NOTHING = 'N'

	CURTIN_STATUS_CHOICES = (
		(ASSOCIATE, 'Associate'),
		(STAFF, 'Staff'),
		(NOTHING, 'Neither/not sure')
	)

	NOTHING = 'NO'
	SOMETHING = 'SO'
	EVERYTHING = 'EV'

	KNOWLEDGE_CHOICES = (
		(NOTHING, 'I know nothing but am keen to learn!'),
		(SOMETHING, 'I know some basics'),
		(EVERYTHING, 'I know a great deal')
	)

	uni = models.CharField(max_length = 50, null = True, blank = True, help_text = "University of study")
	uni_study = models.CharField(max_length = 75, null = True, blank = True, help_text = "If you're attending university, what are you studying?")
	work = models.CharField(max_length = 75, null = True, blank = True, help_text = "If you work, what do you do?")
	contact_number = models.CharField(blank = False, max_length = 10, help_text = "Contact number (mobile preferred)")
	shirt_size = models.CharField(max_length = 3, blank = True, choices = SHIRT_SIZE_CHOICES, help_text = "T-shirt size (for uniform)")
	needs_shirt = models.BooleanField(default = True, help_text = "Does the mentor need to have a shirt provisioned for them?")
	wwcc = models.CharField(max_length = 10, verbose_name = "WWCC card number", blank = True, null = True, help_text = "WWCC card number (if WWCC card holder)")
	wwcc_receipt = models.CharField(max_length = 15, verbose_name = "WWCC receipt number", blank = True, null = True, help_text = "WWCC receipt number (if WWCC is processing)")
	curtin_status = models.TextField(max_length = 1, verbose_name = "Current Curtin HR status", choices = CURTIN_STATUS_CHOICES, blank = False, help_text = "When possible, we recommend that all CoderDojo mentors are either Curtin University Associates or Staff members.")
	curtin_id = models.TextField(max_length = 10, verbose_name = "Curtin Staff/Associate ID", blank = True, null = True, help_text = "Your Curtin Staff/Associate ID (if applicable)")
	coding_experience = models.CharField(max_length = 2, choices = KNOWLEDGE_CHOICES, help_text = "How much programming experience do you have?")
	children_experience = models.CharField(max_length = 2, choices = KNOWLEDGE_CHOICES, help_text = "How much experience do you have with children?")
	roles_desired = models.ManyToManyField(Role)
	user = models.OneToOneField(User, unique = True)

	def name(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)

	def wwcc_status(self):
		if self.wwcc:
			return 'CARD ON RECORD'
		elif self.wwcc_receipt:
			return 'RECEIPT ON RECORD'
		else:
			return 'NOT ON RECORD'
	
	def __unicode__(self):
		return self.name()
