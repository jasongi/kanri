from django.views.generic.edit import CreateView, UpdateView, DeleteView

class KanriCreateView(CreateView):
	template_name = 'generic_form.html'

class KanriUpdateView(UpdateView):
	template_name = 'generic_form.html'
