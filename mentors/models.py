from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
	"""A role somebody can take in a CoderDojo term."""
	name = models.CharField(max_length = 50, blank = False, help_text = "The name of the role.")
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
			(MALE_SMALL, "Male Small"),
			(MALE_MEDIUM, "Male Medium"),
			(MALE_LARGE, "Male Large"),
			(MALE_EXTRA_LARGE, "Male Extra Large")
		)),
		('Female', (
			(FEMALE_EXTRA_SMALL, "Female Extra Small"),
			(FEMALE_SMALL, "Female Small"),
			(FEMALE_MEDIUM, "Female Medium"),
			(FEMALE_LARGE, "Female Large"),
			(FEMALE_EXTRA_LARGE, "Female Extra Large")
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
	student_number = models.CharField(max_length = 15, null = True, blank = True, help_text = 'Student number (if studying)')
	industry = models.CharField(max_length = 50, null = True, blank = True, help_text = "Industry (if any)")
	contact_number = models.CharField(blank = False, max_length = 10, help_text = "Contact number (mobile preferred)")
	shirt_size = models.CharField(max_length = 3, choices = SHIRT_SIZE_CHOICES, help_text = "T-shirt size (for uniform)")
	needs_shirt = models.BooleanField(default = True, help_text = "Does the mentor need to have a shirt provisioned for them?")
	wwcc = models.CharField(max_length = 10, verbose_name = "WWCC card number", blank = True, null = True, help_text = "WWCC card number (if WWCC card holder)")
	wwcc_receipt = models.CharField(max_length = 15, verbose_name = "WWCC receipt number", blank = True, null = True, help_text = "WWCC receipt number (if WWCC is processing)")
	curtin_status = models.TextField(max_length = 1, verbose_name = "Current Curtin HR status", choices = CURTIN_STATUS_CHOICES, blank = False, help_text = "When possible, we recommend that all CoderDojo mentors are either Curtin University Associates or Staff members.")
	curtin_id = models.TextField(max_length = 10, verbose_name = "Curtin Staff/Associate ID", blank = True, null = True, help_text = "Your Curtin Staff/Associate ID (if applicable)")
	first_aid = models.BooleanField(default = False, help_text = "First-aid certificate holder")
	referral = models.CharField(max_length = 50, blank = True, help_text = "How did you hear about us?")
	aim = models.TextField(max_length = 255, blank = True, help_text = "What do you hope to get out of your mentoring experience?")
	coding_experience = models.CharField(max_length = 2, choices = KNOWLEDGE_CHOICES, help_text = "How much programming experience do you have?")
	coding_experience_freeform = models.TextField(max_length = 255, blank = True, null = True, help_text = "Please indicate any specific areas of coding knowledge/interest (eg. Python, HTML)")
	children_experience = models.CharField(max_length = 2, choices = KNOWLEDGE_CHOICES, help_text = "How much experience do you have with children?")
	children_experience_freeform = models.TextField(max_length = 255, blank = True, null = True, help_text = "Please indicate any experience working with young people (eg. tutoring, babysitting, studying education)")
	roles_desired = models.ManyToManyField(Role)
	user = models.OneToOneField(User, unique = True)

	def name(self):
		return "%s %s" % (self.user.first_name, self.user.last_name)

	def wwcc_status(self):
		if (len(self.wwcc) > 0):
			return 'CARD ON RECORD'
		elif len(self.wwcc_receipt) > 0:
			return 'RECEIPT ON RECORD'
		else:
			return 'NOT ON RECORD'
	
	def __unicode__(self):
		return self.name()
