from django.db import models

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

    description = models.CharField(
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

    def __unicode__(self):
        return self.name

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

    def __unicode__(self):
        return "%s on %s" % (self.mentor, self.job)