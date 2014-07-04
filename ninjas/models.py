from django.db import models
from django.core.urlresolvers import reverse
from kanri import knowledge

class Parent(models.Model):
    name = models.CharField(
        blank = False,
        help_text = "Full name",
        max_length = 50
    )

    email = models.EmailField(
        blank = False,
        unique = True,
        max_length = 254,
        help_text = 'Contact email address'
    )

    phone = models.PositiveIntegerField(
        blank = False,
        max_length = 10,
        help_text = 'Contact phone number (mobile preferred)'
    )

class Ninja(models.Model):
    name = models.CharField(
        max_length = 30,
        blank = False,
        help_text = 'What is the Ninja\'s name?'
    )

    email = models.EmailField(
        max_length = 254,
        help_text = 'Ninja\'s email (if they have one)'
    )

    postcode = models.PositiveIntegerField(
        blank = False,
        max_length = 4,
        help_text = 'Postcode (for statistical purposes)'
    )

    school = models.CharField(
        max_length = 50,
        blank = False,
        help_text = 'What school does the Ninja attend?'
    )

    school_year = models.PositiveSmallIntegerField(
        blank = False,
        default = 7,
        help_text = 'What school year is the Ninjas in?'
    )

    allergies = models.CharField(
        max_length = 140,
        blank = True,
        help_text = 'Allergies/Dietary Restrictions'
    )

    attended_workshop = models.BooleanField(
        default = False,
        help_text = 'Has the Ninja attended a CoderDojo workshop before?'
    )

    referral = models.CharField(
        max_length = 140,
        blank = True,
        help_text = 'How did you hear about CoderDojo?'
    )

    laptop = models.BooleanField(
        default = False,
        help_text = "Does the Ninja have a laptop they can bring to their CoderDojo sessions?"
    )

    aim = models.TextField(
        max_length = 255,
        blank = True,
        help_text = "What do you hope to get out of CoderDojo?"
    )

    general_knowledge = models.CharField(
        choices = knowledge.KNOWLEDGE_CHOICES,
        max_length = 2,
        default = knowledge.NOTHING,
        help_text = "How much do you know about coding in general?"
    )

    scratch_knowledge = models.CharField(
        choices = knowledge.KNOWLEDGE_CHOICES,
        max_length = 2,
        default = knowledge.NOTHING,
        help_text = "How much do you know about Scratch?"
    )

    codecademy_knowledge = models.CharField(
        choices = knowledge.KNOWLEDGE_CHOICES,
        max_length = 2,
        default = knowledge.NOTHING,
        help_text = "How much do you know about Codecademy?"
    )

    language_experience = models.TextField(
        max_length = 140,
        null = True,
        blank = True,
        help_text = 'If you have experience with coding, what types of languages have you used?'
    )

    black_belt = models.BooleanField(
        default = False,
        help_text = "Want to be a 'Black Belt' Ninja? If you've participated in a CoderDojo WA workshop before, \
        and you'd like to help out as a mentor for new students, let us know!"
    )

    photo_release = models.BooleanField(
        default = True,
        help_text = "I give permission for CoderDojo WA, Curtin University,and Curtin University's student-run \
        Computer Science Students Association (ComSSA) to use photographs of my child for publicity purposes."
    )

    parent = models.ForeignKey(
        Parent,
        help_text = 'Ninja\'s parent information'
    )

    availabilities = models.ManyToManyField('planner.DojoSession')

    def parent_required(self):
        return self.school_year <= 6

    def get_absolute_url(self):
        return reverse('detail', current_app = 'ninjas', args = [self.id])

    def __unicode__(self):
        return self.name