from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape

register = template.Library()

@register.filter(needs_autoescape=True)
def display_pair(field, name, autoescape = None):
	if autoescape is not True:
		raise ValueError("Auto escaping must be turned off for this filter to work")

	markup = """
	<div class="form-group">
		<label class="col-sm-2 control-label">%s</label>
		<div class="col-sm-10">
			<p class="form-control-static">%s</p>
		</div>
	</div> """ % (name, escape(field))

	return mark_safe(markup)

