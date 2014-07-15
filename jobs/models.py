from django.db import models
from django.core.urlresolvers import reverse_lazy

class Job(models.Model):
    BEFORE = 'B'
    DURING = 'D'
    AFTER = 'A'

    TIME_CHOICES = (
        (BEFORE, 'Before session'),
        (DURING, 'During session'),
        (AFTER, 'After session'),
    )

    name = models.CharField(
        max_length = 50,
        help_text = "The job's name."
    )

    description = models.TextField(
        max_length = 1024,
        help_text = "A description of the job."
    )
    
    location = models.CharField(
        max_length = 50,
        help_text = "The job's location."
    )

    time = models.CharField(
        max_length = 1,
        choices = TIME_CHOICES,
        help_text = "The time during a session at which this job can be carried out."
    )

    def get_absolute_url(self):
    	return reverse_lazy('jobs:detail', args = [self.id])

    def __unicode__(self):
        return self.name

    class Meta():
        permissions = {
            ('read_job', "Can view a Job entry"),
            ('register_for_job', 'Can register themselves a job'),
        }

class JobAllocation(models.Model):
    job = models.ForeignKey(Job,
        help_text = "The job the mentor will be performing."
    )

    mentor = models.ForeignKey('mentors.Mentor',
        help_text = "The mentor that'll be undertaking the job."
    )

    session = models.ForeignKey('planner.DojoSession',
        help_text = "The session during which this job allocation will take place."
    )

    class Meta():
        permissions = {
            ('read_joballocation', "Can view a JobAllocation entry"),
        }

    def __unicode__(self):
        return "%s on %s" % (self.mentor, self.job)