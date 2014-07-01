from django.shortcuts import render, get_object_or_404
from mentors.models import Mentor, Role
from forms import CSVImportForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from kanri.views import KanriCreateView, KanriUpdateView, KanriDetailView
import csv

def index(request):
	success = None
	if request.method == "POST":
		form = CSVImportForm(request.POST, request.FILES)
		if form.is_valid():
			# form is valid, start parsing CSV.
			# First detect dialect
			csvfile = request.FILES['csv']
			dialect = csv.Sniffer().sniff(csvfile.read(2048))
			csvfile.seek(0)
			# Open reader.
			reader = csv.DictReader(csvfile, dialect=dialect)
			# Parse each row.
			for row in reader:
				# first, check if mentor already exists.
				same = Mentor.objects.filter(user__email = row['Email address'])
				if (same):
					m = same[0]
					print "Existing mentor %s" % row['Full name']
				else:
					print "New mentor %s" % row['Full name']
					m = Mentor()

					# Check to see if a non-mentor user exists with the mentor's email
					same = get_user_model().objects.filter(email = row['Email address'])
					if (same):
						m.user = same[0]
					else:
						pwd = get_user_model().objects.make_random_password()
						print "Password for %s: %s" % (row['Full name'], pwd)
						name_array = row['Full name'].split(' ', 1)
						m.user = get_user_model().objects.create_user(row['Email address'], name_array[0], name_array[1], pwd)
						m.user.save()

				# Add contact number
				m.user.phone_number = '0' + row['Mobile number']

				# Add new user to mentors group
				group = Group.objects.get_or_create(name='Mentors')
				m.user.groups.add(group[0])

				m.user.save()

				# University
				if 'University' in row:
					m.uni = row['University']

				# Study
				if 'Study' in row:
					m.uni_study = row['Study']

				# Work
				if 'Work' in row:
					m.work = row['Work']
				
				# shirt size mapping
				ts = row['T-shirt size']
				if ts == 'I already have a CoderDojo WA tshirt':
					m.needs_shirt = False
				elif ts == 'Male S':
					m.shirt_size = Mentor.MALE_SMALL
				elif ts == 'Male M':
					m.shirt_size = Mentor.MALE_MEDIUM
				elif ts == 'Male L':
					m.shirt_size = Mentor.MALE_LARGE
				elif ts == 'Male XL':
					m.shirt_size = Mentor.MALE_EXTRA_LARGE
				elif ts == 'Female XS':
					m.shirt_size = Mentor.FEMALE_EXTRA_SMALL
				elif ts == 'Female S':
					m.shirt_size = Mentor.FEMALE_SMALL
				elif ts == 'Female M':
					m.shirt_size = Mentor.FEMALE_MEDIUM
				elif ts == 'Female L':
					m.shirt_size = Mentor.FEMALE_LARGE
				elif ts == 'Female XL':
					m.shirt_size = Mentor.FEMALE_EXTRA_LARGE

				# WWCC
				if 'WWCC Number' in row:
					m.wwcc = row['WWCC Number']

				# Curtin status
				curtin_status = row['Curtin Status']
				if curtin_status == 'Associate':
					m.curtin_status = Mentor.ASSOCIATE
				elif curtin_status == 'Staff':
					m.curtin_status = Mentor.STAFF
				elif curtin_status == 'Neither/Not Sure':
					m.curtin_status = Mentor.NEITHER

				# Associate/Staff ID
				if 'Curtin Associate/Staff ID' in row:
					m.curtin_id = row['Curtin Associate/Staff ID']

				# Coding experience
				coding_xp = row['Coding Experience']
				if coding_xp == 'I know nothing but am keen to learn!':
					m.coding_experience = Mentor.NOTHING
				elif coding_xp == 'I know some basics':
					m.coding_experience = Mentor.SOMETHING
				elif coding_xp == 'I know a great deal':
					m.coding_experience = Mentor.EVERYTHING

				# Child-related experience
				children_xp = row['Child-Related Experience']
				if children_xp == 'I know nothing but am keen to learn!':
					m.children_experience = Mentor.NOTHING
				elif children_xp == 'I know some basics':
					m.children_experience = Mentor.SOMETHING
				elif children_xp == 'I know a great deal':
					m.children_experience = Mentor.EVERYTHING

				# Gotta save before you can do M2M relations.
				m.save()
				for role in Role.objects.all():
					if role.name in row['Roles'].decode('utf-8') and role not in m.roles_desired.all():
						m.roles_desired.add(role)
				m.save()
			success = True
		else:
			success = False
	else:
		form = CSVImportForm()
	return render(request, 'mentors/index.html', {
			'mentors': Mentor.objects.order_by('user__first_name'),
			'roles': Role.objects.all(),
			'form': form,
			'success': success,
		})

def role_index(request):
	return render(request, 'mentors/role_index.html', {
		'roles': Role.objects.order_by('name'),
	})

class MentorCreate(KanriCreateView):
	model = Mentor

class MentorUpdate(KanriUpdateView):
	model = Mentor

class RoleCreate(KanriCreateView):
	model = Role

class RoleUpdate(KanriUpdateView):
	model = Role
	#success_url = reverse('mentors.index')

class RoleDetail(KanriDetailView):
	model = Role
	template_name = 'mentors/role_detail.html'

def detail(request, blazeit):
	return 1;