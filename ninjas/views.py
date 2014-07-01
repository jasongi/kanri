from django.shortcuts import render, get_object_or_404
from ninjas.models import Ninja
from django.http import HttpResponse
from kanri.views import KanriCreateView, KanriUpdateView, KanriListView
from django.core.urlresolvers import reverse_lazy

class NinjaCreate(KanriCreateView):
	model = Ninja
	#fields = ['name']

class NinjaUpdate(KanriUpdateView):
	model = Ninja

class NinjaList(KanriListView):
	model = Ninja
	template_name = 'ninjas/index.html'

# Create your views here.
def index(request):
	return render(request, 'ninjas/index.html', {
			'ninjas': Ninja.objects.order_by('name')
		})

def detail(request, ninja_id):
	ninja = get_object_or_404(Ninja, pk = ninja_id)
	return render(request, 'ninjas/detail.html', {
			'ninja': ninja
		})