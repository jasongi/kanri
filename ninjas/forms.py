from django import forms
import csv
from csvvalidator import *

class CSVImportForm(forms.Form):
	csv = forms.FileField(required = True, label = "CSV file", help_text = "A valid CSV file from the CoderDojo @ Curtin ninja signup sheet.")

	def is_valid(self):
		csvfile = self.files.get('csv')
		try:
			dialect = csv.Sniffer().sniff(csvfile.read(2048))
		except csv.Error:
			return False
		csvfile.seek(0)
		reader = csv.reader(csvfile, dialect=dialect)		
		fields = (
			"Timestamp",
			"Full Name",
			"School",
			"School Year",
			"Email Address",
			"Gender ",
			"Been Before?",
			"Black Belt",
			"Referral",
			"Laptop",
			"Aim",
			"Coding Knowledge",
			"Codecademy Knowledge",
			"Scratch Knowledge",
			"Programming Languages",
			"Parent/Guardian Name",
			"Phone Number",
			"Postcode",
			"Parent/Guardian Email",
			"Allergies/Dietary Restrictions",
			"Photo Permission",
			"Parent's Permission",
			"Availability [Saturday 2 August]",
			"Availability [Saturday 9 August]",
			"Availability [Saturday 16 August]",
			"Availability [Saturday 23 August]",
			"Availability [Saturday 30 August]",
			"Availability [Saturday 6 September]",
			"Availability [Saturday 13 September]",
			"Availability [Saturday 20 September]",
		)

		val = CSVValidator(fields)

		val.add_header_check('EX1', 'bad header')
		val.add_record_length_check('EX2', 'unexpected record length')
		status = val.validate(reader)
		csvfile.seek(0)
		if len(status) is 0:
			return True
		else:
			return False