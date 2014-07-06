from django import forms
from planner.models import DojoTerm, Room

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