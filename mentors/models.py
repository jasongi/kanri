from django.db import models
from django.contrib.auth.models import User

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
	first_aid = models.BooleanField(default = False, help_text = "First-aid certificate holder")
	referral = models.CharField(max_length = 50, blank = True, help_text = "How did you hear about us?")
	aim = models.TextField(max_length = 255, blank = True, help_text = "What do you hope to get out of your mentoring experience?")
	coding_experience = models.CharField(max_length = 2, choices = KNOWLEDGE_CHOICES, help_text = "How much programming experience do you have?")
	children_experience = models.CharField(max_length = 2, choices = KNOWLEDGE_CHOICES, help_text = "How much experience do you have with children?")
	children_experience_freeform = models.TextField(max_length = 255, blank = True, null = True, help_text = "Please indicate any experience working with young people (eg. tutoring, babysitting, studying education)")
	wants_champion = models.BooleanField(default = False, help_text = "Do you wish to apply for the Champion role?")
	wants_lead = models.BooleanField(default = False, help_text = "Do you wish to apply for a Lead Mentor position?")
	wants_support = models.BooleanField(default = False, help_text = "Do you wish to apply for a Support Mentor position?")
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
