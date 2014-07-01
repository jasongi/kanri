from django import template

register = template.Library()

def name(view):
	return view.model.__name__

register.filter('name', name)
