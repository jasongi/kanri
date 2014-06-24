from django.shortcuts import render, get_object_or_404
from mentors.models import Mentor

def index(request):
	return render(request, 'mentors/index.html', {
			'mentors': Mentor.objects.order_by('user__first_name')[:3]
		})
