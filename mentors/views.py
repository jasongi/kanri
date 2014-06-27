from django.shortcuts import render, get_object_or_404
from mentors.models import Mentor
from forms import CSVImportForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	success = None
	if request.method == "POST":
		form = CSVImportForm(request.POST, request.FILES)
		if form.is_valid():
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
