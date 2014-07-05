from django.shortcuts import render, get_object_or_404
from ninjas.models import Ninja, Parent
from django.http import HttpResponse
from kanri.views import KanriCreateView, KanriUpdateView, KanriListView
from ninjas.forms import CSVImportForm
from django.core.urlresolvers import reverse_lazy
from kanri import csv_tools, knowledge
import csv

def index(request):
	return render(request, 'ninjas/index.html', {
		'ninja_stats' : Ninja.get_stats(),
		'parent_stats': Parent.get_stats()
		})

class NinjaCreate(KanriCreateView):
	model = Ninja

class NinjaUpdate(KanriUpdateView):
	model = Ninja

class NinjaList(KanriListView):
	model = Ninja
	template_name = 'ninjas/list.html'

def upload(request):
	if request.method == 'POST':
		form = CSVImportForm(request.POST, request.FILES)
		if not form.is_valid():
			return render(request, 'ninjas/upload/failure.html')
		else:
			# form is valid, start parsing CSV.
			# First detect dialect
			csvfile = request.FILES['csv']
			dialect = csv.Sniffer().sniff(csvfile.read(2048))
			csvfile.seek(0)
			# Open reader and parse each row.
			reader = csv.DictReader(csvfile, dialect=dialect)
			for row in reader:
				# First, check if Ninja exists.
				same = Ninja.objects.filter(name = row['Full Name'])

				if same:
					ninja = same[0]
					print "Existing ninja: %s" % ninja.name
				else:
					ninja = Ninja(name = row['Full Name'])
					print "New ninja: %s" % ninja.name

				gender = row['Gender']
				if gender == 'Male':
					gender = ninja.MALE
				elif gender == 'Female':
					gender = ninja.FEMALE

				print "\tGender was: %s" % row['Gender']
				print "\tWe ended up with: %s" % gender

				ninja.gender = gender

				ninja.email = row['Email Address']
				ninja.school = row['School']
				ninja.school_year = row['School Year']
				ninja.postcode = row['Postcode']
				ninja.allergies = csv_tools.none_catch(row['Allergies/Dietary Restrictions'])
				ninja.attended_workshop = csv_tools.yes_no(row['Been Before?'])
				ninja.referral = row['Referral']
				ninja.laptop = csv_tools.yes_no(row['Laptop'])
				ninja.aim = row['aim'] = row['Aim']
				ninja.general_knowledge = csv_tools.knowledge_parse(row['Coding Knowledge'])
				ninja.scratch_knowledge = csv_tools.knowledge_parse(row['Scratch Knowledge'])
				ninja.codecademy_knowledge = csv_tools.knowledge_parse(row['Codecademy Knowledge'])
				ninja.language_experience = row['Programming Languages']
				ninja.black_belt = csv_tools.yes_no(row['Black Belt'], fuzzy = True)
				ninja.photo_release = csv_tools.yes_no(row['Photo Permission'], fuzzy = True)

				# Now for the parent/guardian
				same = Parent.objects.filter(email = row['Parent/Guardian Email'])
				if same:
					pa = same[0]
				else:
					pa = Parent(email = row['Parent/Guardian Email'])

				pa.name = row['Parent/Guardian Name']
				pa.phone = row['Phone Number']
				pa.save()
				ninja.parent = pa
				ninja.save()

			return render(request, 'ninjas/upload/success.html')
	else:		
		return render(request, 'ninjas/upload/failure.html')

def detail(request, ninja_id):
	ninja = get_object_or_404(Ninja, pk = ninja_id)
	return render(request, 'ninjas/detail.html', {
			'ninja': ninja
		})