from django.db import models
from django.core.urlresolvers import reverse

class Contact(models.Model):
	name = models.CharField(max_length = 30, blank = False, help_text = "What is the contact's name?")
	phone = models.PositiveIntegerField(blank = False, help_text = "What's this contact's primary contact number?")
	email = models.EmailField(max_length = 254, blank = True, help_text = 'If this contact wishes to receive important information (e.g. room changes, parking information), please record their email address.')
	relationship = models.CharField(max_length = 20, blank = False, help_text = "What relationship does this contact have with the Ninja?")
	related_ninja = models.ForeignKey('Ninja')

class Ninja(models.Model):
	WEBSITE = 'WS'
	FRIEND = 'FR'
	SCHOOL = 'SC'
	FACEBOOK = 'FB'
	OTHER = 'OT'

	REFERRAL_CHOICES = (
		(WEBSITE, 'From the CoderDojo WA website'),
		(FRIEND, 'From a friend'),
		(SCHOOL, 'From my school'),
		(FACEBOOK, 'From CoderDojo WA\'s Facebook Page'),
		(OTHER, 'Other')
	)

	NOTHING = 'NO'
	SOMETHING = 'SO'
	EVERYTHING = 'EV'

	KNOWLEDGE_CHOICES = (
		(NOTHING, 'Beginner'),
		(SOMETHING, 'Intermediary'),
		(EVERYTHING, 'Advanced')
	)

	#class Meta():
	#	verbose_name_plural = 'Ninjas'

	name = models.CharField(max_length = 30, blank = False, help_text = 'What is the Ninja\'s name?')
	school = models.CharField(max_length = 50, blank = False, help_text = 'What school does the Ninja attend?')
	school_year = models.PositiveSmallIntegerField(blank = False, help_text = 'What school year is the Ninjas in?')
	attended_workshop = models.BooleanField(default = False, help_text = 'Has the Ninja attended a CoderDojo workshop before?')
	referral = models.CharField(choices = REFERRAL_CHOICES, max_length = 2, default = OTHER, help_text = 'How did you hear about CoderDojo?')
	laptop = models.BooleanField(default = False, help_text = "Does the Ninja have a laptop they can bring to their CoderDojo sessions?")
	aim = models.TextField(max_length = 255, blank = True, help_text = "What do you hope to get out of CoderDojo?")
	general_knowledge = models.CharField(choices = KNOWLEDGE_CHOICES, max_length = 2, default = NOTHING, help_text = "How much do you know about coding in general?")
	scratch_knowledge = models.CharField(choices = KNOWLEDGE_CHOICES, max_length = 2, default = NOTHING, help_text = "How much do you know about Scratch?")
	codecademy_knowledge = models.CharField(choices = KNOWLEDGE_CHOICES, max_length = 2, default = NOTHING, help_text = "How much do you know about Codecademy?")
	language_experience = models.TextField(max_length = 140, null = True, blank = True, help_text = 'If you have experience with coding, what types of languages have you used?')
	black_belt = models.BooleanField(default = False, help_text = "Want to be a 'Black Belt' Ninja? If you've participated in a CoderDojo WA workshop before, and you'd like to help out as a mentor for new students, let us know!")
	photo_release = models.BooleanField(default = True, help_text = "I give permission for CoderDojo WA to use photographs of my child for publicity purposes.")

	def parent_required(self):
		return self.school_year <= 6

	def get_absolute_url(self):
		return reverse('detail', current_app = 'ninjas', args = [self.id])

	def __unicode__(self):
		return self.name