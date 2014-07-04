from django.contrib import admin
from ninjas.models import Ninja


class NinjaAdmin(admin.ModelAdmin):
	list_display = ('name', 'school', 'school_year', 'attended_workshop', 'referral', 'laptop', 'aim', 'general_knowledge',
		'scratch_knowledge', 'codecademy_knowledge', 'language_experience', 'black_belt', 'photo_release')

	list_filter = ('school', 'school_year', 'attended_workshop', 'laptop', 'general_knowledge', 'scratch_knowledge', 'codecademy_knowledge',
		'black_belt', 'photo_release')

	fieldsets = [
		('Personal Information', {'fields': ['name', 'school', 'school_year', 'photo_release']}),
		('At CoderDojo', {'fields': ['referral', 'laptop', 'attended_workshop', 'aim', 'black_belt']}),
		('Knowledge', {'fields': ['general_knowledge', 'scratch_knowledge', 'codecademy_knowledge', 'language_experience']}),
	]

admin.site.register(Ninja, NinjaAdmin)