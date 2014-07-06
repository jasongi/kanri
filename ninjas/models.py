from django.db import models
from django.core.urlresolvers import reverse
from kanri import knowledge
from django.conf import settings
import auspost

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

    # Statistics Functions #
    @classmethod
    def get_stats(cls):
        stats = {
            'all': cls.objects.count()
        }

        return stats


class Ninja(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    name = models.CharField(
        max_length = 30,
        blank = False,
        help_text = 'What is the Ninja\'s name?'
    )

    email = models.EmailField(
        max_length = 254,
        help_text = 'Ninja\'s email (if they have one)'
    )

    gender = models.CharField(
        max_length = 1,
        choices = GENDER_CHOICES,
        blank = False
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
        null = True,
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

    def get_suburb_list(self):
        ap = auspost.API(settings.AUSPOST_KEY, debug = True)
        locality_list = ap.postcode_search(self.postcode)['localities']['locality']
        
        if not isinstance(locality_list, list):
            locality_list = [locality_list]
        
        locations = []
        for locality in locality_list:
            locations.append(locality['location'])

        return locations

    def get_suburb(self):
        return self.get_suburb_list()[0]

    def get_short_name(self):
        return self.name.split()[0]

    def get_call_url(self):
        return "tel:%s" % self.parent.phone

    def get_email_url(self):
        return "mailto:%s" % self.parent.email
    
    def parent_required(self):
        return self.school_year <= 6

    # Statistics Functions #
    @classmethod
    def get_new(self):
        return self.objects.filter(attended_workshop = False).count()

    @classmethod
    def get_returning(self):
        return self.objects.filter(attended_workshop = True).count()

    @classmethod
    def get_allergies(self):
        return self.objects.exclude(allergies = None)

    @classmethod
    def get_photos(self):
        return self.objects.exclude(photo_release = True)

    @classmethod
    def get_male(cls):
        print cls.objects.filter(gender = cls.MALE)
        return cls.objects.filter(gender = cls.MALE).count()

    @classmethod
    def get_female(cls):
        return cls.objects.filter(gender = cls.FEMALE).count()

    @classmethod
    def get_stats(cls):
        stats = {
            'all': cls.objects.count(),
            'returning': cls.get_returning(),
            'new': cls.get_new(),
            'allergies': cls.get_allergies(),
            'photos': cls.get_photos(),
            'gender': {
                'male': cls.get_male(),
                'female': cls.get_female(),
            },
            'knowledge': {
                'general': {},
                'scratch': {},
                'codecademy': {},
            },
            'black_belts': cls.objects.filter(black_belt = True),
        }

        # Do knowledge stats.
        for choice in knowledge.KNOWLEDGE_CHOICES:
            stats['knowledge']['general'][choice[1]] = cls.objects.filter(general_knowledge = choice[0]).count()
            stats['knowledge']['scratch'][choice[1]] = cls.objects.filter(scratch_knowledge = choice[0]).count()
            stats['knowledge']['codecademy'][choice[1]] = cls.objects.filter(codecademy_knowledge = choice[0]).count()

        return stats

    def get_absolute_url(self):
        return reverse('ninjas:detail', current_app = 'ninjas', args = [self.id])

    def __unicode__(self):
        return self.get_short_name()