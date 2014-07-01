from django import template

register = template.Library()

def name(model):
	return model.__name__

def model_name(view):
	return name(view.model)

def class_name(model):
	return name(model.__class__)


register.filter('name', name)
register.filter('model_name', model_name)
register.filter('class_name', class_name)
