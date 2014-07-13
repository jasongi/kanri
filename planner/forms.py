from django import forms
from planner.models import DojoTerm, Room
from mentors.models import Mentor

class DojoTermForm(forms.Form):
	name = forms.CharField(
		max_length = 50,
		help_text = "A human-readable name for the term.",
	)

	first_session_date = forms.DateField(
		help_text = "The starting date and time of the first session.",
	)
 
	first_session_start = forms.TimeField(
		help_text = "The start time of the first session.",
		input_formats = ['%I:%M %p']
	)

	first_session_end = forms.TimeField(
		help_text = "The end time of the first session.",
		input_formats = ['%I:%M %p']
	)

	rooms = forms.ModelMultipleChoiceField(
		queryset = Room.objects.all(),
		help_text = 'What rooms are available for use during this term?'
	)

	weeks = forms.IntegerField(
		min_value = 1,
		help_text = "The number of weeks the term will run.",
	)

class ShiftAllocationForm(forms.Form):	
	def __init__(self, *args, **kwargs):
		# Grab the custom kwargs out before we call super init.
		# I'm gross, but it stops the strict super.__init__ from crying.
		session = kwargs.pop('session', None)
		role = kwargs.pop('role', None)
		super(ShiftAllocationForm, self).__init__(*args, **kwargs)
		
		self.fields['mentor'] = forms.ModelChoiceField(
			queryset = Mentor.objects.filter(
				shift_availabilities = session,
				roles_desired = role
			)
		)

		self.fields['room'] = forms.ModelChoiceField(
			queryset = session.rooms.all(),
			required = False
		)

		self.fields['start'] = forms.TimeField(
			input_formats = ['%I:%M %p'],
			initial = session.start,
			widget = forms.TimeInput(
				format = '%I:%M %p'
			)
		)

		self.fields['end'] = forms.TimeField(
			input_formats = ['%I:%M %p'],
			initial = session.end,
			widget = forms.TimeInput(
				format = '%I:%M %p'
			)
		)

class JobAllocationForm(forms.Form):
	def __init__(self, *args, **kwargs):
		# Grab the custom kwargs out before we call super init.
		# I'm gross, but it stops the strict super.__init__ from crying.
		session = kwargs.pop('session', None)
		job = kwargs.pop('job', None)\

		super(JobAllocationForm, self).__init__(*args, **kwargs)
	
		self.fields['mentors'] = forms.ModelMultipleChoiceField(
			queryset = Mentor.objects.filter(
				shift_availabilities = session
			).exclude(
				joballocation__session = session
			)
		)