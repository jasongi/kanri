from django.contrib import admin
from mentors.models import Mentor

class MentorAdmin(admin.ModelAdmin):
	list_display = ('name', 'shirt_size', 'wwcc_status', 'first_aid', 'wants_champion', 'wants_lead', 'wants_support')

	list_filter = ('first_aid', 'wants_champion', 'wants_lead', 'wants_support', 'shirt_size')

	fieldsets = [
		('Personal Information', {'fields': ['contact_number', 'shirt_size']}),
		('Industry Information', {'fields': ['uni', 'student_number', 'industry']}),
		('Qualifications', {'fields': ['wwcc', 'wwcc_receipt', 'first_aid']}),
		('Knowledge and Experience', {'fields': ['coding_experience', 'children_experience', 'children_experience_freeform']}),
		('Aim', {'fields': ['aim', 'wants_champion', 'wants_lead', 'wants_support', 'referral']}),
		('Administration', {'fields': ['user']}),
	]

admin.site.register(Mentor, MentorAdmin)