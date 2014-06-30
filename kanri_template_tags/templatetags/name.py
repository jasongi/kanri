from django import template

register = template.Library()

def name(target):
	return target.__class__.__name__

register.filter('name', name)
