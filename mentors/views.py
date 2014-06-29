from django.shortcuts import render, get_object_or_404
from mentors.models import Mentor, Role
from forms import CSVImportForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, BaseUserManager
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
				if (len(same) > 0):
					existing = same[0]
					print "Existing user %s" % row['Full name']
				else:
					m = Mentor()
					m.user = User.objects.create_user(row['Email address'], row['Email address'], User.objects.make_random_password())
					name_array = row['Full name'].split(' ', 1)
					m.user.first_name = name_array[0]
					m.user.last_name = name_array[1]
					m.user.save()
					if 'University' in row:
						m.uni = row['University']

					if 'Study' in row:
						m.uni_study = row['Study']

					if 'Work' in row:
						m.work = row['Work']

					m.contact_number = int('0' + row['Mobile number'])
					
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
					else:
						raise ValueError("Unknown shirt size: %s" % ts)
					if 'WWCC Number' in row:
						m.wwcc = row['WWCC Number']

					curtin_status = row['Curtin Status']
					if curtin_status == 'Associate':
						m.curtin_status = Mentor.ASSOCIATE
					elif curtin_status == 'Staff':
						m.curtin_status = Mentor.STAFF
					elif curtin_status == 'Neither/Not Sure':
						m.curtin_status = Mentor.NOTHING

					if 'Curtin Associate/Staff ID' in row:
						m.curtin_id = row['Curtin Associate/Staff ID']

					coding_xp = row['Coding Experience']
					if coding_xp == 'I know nothing but am keen to learn!':
						m.coding_experience = Mentor.NOTHING
					elif coding_xp == 'I know some basics':
						m.coding_experience = Mentor.SOMETHING
					elif coding_xp == 'I know a great deal':
						m.coding_experience = Mentor.EVERYTHING

					# DRY is for scrubs
					children_xp = row['Coding Experience']
					if children_xp == 'I know nothing but am keen to learn!':
						m.children_experience = Mentor.NOTHING
					elif children_xp == 'I know some basics':
						m.children_experience = Mentor.SOMETHING
					elif children_xp == 'I know a great deal':
						m.children_experience = Mentor.EVERYTHING

					m.save()

					for role in Role.objects.all():
						if role.name in row['Roles']:
							m.roles_desired.add(role)

					m.save()
			success = True
		else:
			success = False
	else:
		form = CSVImportForm()

	return render(request, 'mentors/index.html', {
			'mentors': Mentor.objects.order_by('user__first_name')[:3],
			'form': form,
			'success': success,
		})

def upload(request):
	return 1;

def add(request):
	return 1;
