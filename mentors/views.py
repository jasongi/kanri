from django.shortcuts import render, get_object_or_404
from mentors.models import Mentor, Role
from planner.models import DojoSession
from forms import CSVImportForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
from kanri.views import *
import datetime
import csv

## Mentor ## 
def upload(request):
	stats = {
		'total': 0,
		'new_mentors': 0,
		'new_users': 0,
	}

	if request.method == "POST":
		form = CSVImportForm(request.POST, request.FILES)
		if form.is_valid():
			# form is valid, start parsing CSV.
			sessions = {
				'2 August': DojoSession.objects.get(date = datetime.date(2014, 8, 2)),
				'9 August': DojoSession.objects.get(date = datetime.date(2014, 8, 9)),
				'16 August': DojoSession.objects.get(date = datetime.date(2014, 8, 16)),
				'23 August': DojoSession.objects.get(date = datetime.date(2014, 8, 23)),
				'30 August': DojoSession.objects.get(date = datetime.date(2014, 8, 30)),
				'6 September': DojoSession.objects.get(date = datetime.date(2014, 9, 6)),
				'13 September': DojoSession.objects.get(date = datetime.date(2014, 9, 13)),
				'20 September': DojoSession.objects.get(date = datetime.date(2014, 9, 20)),
			}

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
					stats
				else:
					print "New mentor %s" % row['Full name']
					m = Mentor()
					stats['new_mentors'] += 1

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
						stats['new_users'] += 1

				# Add contact number
				m.user.phone_number = '0' + row['Mobile number']

				# Add new user to mentors group
				group = Group.objects.get_or_create(name = 'Mentors')
				m.user.groups.add(group[0])

				m.user.save()
				m.uni = csv_tools.none_catch(row['University'])
				m.uni_study = csv_tools.none_catch(row['Study'])
				m.work = csv_tools.none_catch(row['Work'])
				
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
				m.wwcc = csv_tools.none_catch(row['WWCC Number'])

				# Curtin status
				curtin_status = row['Curtin Status']
				if curtin_status == 'Associate':
					m.curtin_status = Mentor.ASSOCIATE
				elif curtin_status == 'Staff':
					m.curtin_status = Mentor.STAFF
				elif curtin_status == 'Neither/Not Sure':
					m.curtin_status = Mentor.NEITHER

				m.curtin_id = csv_tools.none_catch(row['Curtin Associate/Staff ID'])

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

				# Roles
				for role in Role.objects.all():
					if role.name in row['Roles'].decode('utf-8') and role not in m.roles_desired.all():
						m.roles_desired.add(role)

				# Shift Availabilities
				for session in sessions:
					if row['Availability [Saturday %s]' % session] == 'Available':
						m.shift_availabilities.add(sessions[session])

				m.save()

				stats['total'] += 1

	if stats['total'] > 0:
		return render(request, 'mentors/upload/success.html', {
			'stats': stats,
		})
	else:
		return render(request, 'mentors/upload/failure.html')

class MentorCreate(KanriCreateView):
	model = Mentor

class MentorList(KanriListView):
	model = Mentor
	template_name = 'mentors/index.html'

	def get_context_data(self, **kwargs):
		context = super(MentorList, self).get_context_data(**kwargs)
		context['roles'] = Role.objects.order_by('name')
		return context

class MentorDetail(KanriDetailView):
	model = Mentor
	template_name = 'mentors/detail.html'

class MentorUpdate(KanriUpdateView):
	model = Mentor

class MentorDelete(KanriDeleteView):
	model = Mentor
	success_url = reverse_lazy('mentors:index')

## Role ##
class RoleCreate(KanriCreateView):
	model = Role

class RoleDetail(KanriDetailView):
	model = Role
	template_name = 'mentors/role_detail.html'

class RoleList(KanriListView):
	model = Role
	template_name = 'mentors/role_index.html'

class RoleUpdate(KanriUpdateView):
	model = Role

class RoleDelete(KanriDeleteView):
	model = Role
	success_url = reverse_lazy('mentors:role-index')