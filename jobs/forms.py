from django import forms
from mentors.models import Mentor

class JobAllocationForm(forms.Form):
	def __init__(self, *args, **kwargs):
		# Grab the custom kwargs out before we call super init.
		# I'm gross, but it stops the strict super.__init__ from crying.
		session = kwargs.pop('session', None)
		job = kwargs.pop('job', None)

		super(JobAllocationForm, self).__init__(*args, **kwargs)
	
		self.fields['mentors'] = forms.ModelMultipleChoiceField(
			queryset = Mentor.objects.filter(
				shift_availabilities = session,
				jobs_desired = job
			).exclude(
				joballocation__session = session,
				joballocation__job__time = job.time,
			)
		)