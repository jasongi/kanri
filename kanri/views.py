from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

class KanriCreateView(CreateView):
	template_name = 'generic_form.html'

class KanriUpdateView(UpdateView):
	template_name = 'generic_form.html'

class KanriDetailView(DetailView):
	template_name = 'generic_detail.html'