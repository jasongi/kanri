from django import forms

class CSVImportForm(forms.Form):
	csv = forms.FileField(required = True, label = "CSV file", help_text = "A valid CSV file from the CoderDojo @ Curtin mentor signup sheet.")