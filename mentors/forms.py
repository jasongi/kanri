from django import forms
import csv
from csvvalidator import *

class CSVImportForm(forms.Form):
	csv = forms.FileField(required = True, label = "CSV file", help_text = "A valid CSV file from the CoderDojo @ Curtin mentor signup sheet.")

	def is_valid(self):
		csvfile = self.files.get('csv')
		dialect = csv.Sniffer().sniff(csvfile.read(2048))
		csvfile.seek(0)
		reader = csv.reader(csvfile, dialect=dialect)		
		fields = (
			"Timestamp",
			"Full name",
			"Email address",
			"Roles",
			"Availability [Saturday 2 August]",
			"Availability [Saturday 9 August]",
			"Availability [Saturday 16 August]",
			"Availability [Saturday 23 August]",
			"Availability [Saturday 30 August]",
			"Availability [Saturday 6 September]",
			"Availability [Saturday 13 September]",
			"Availability [Saturday 20 September]",
			"Mobile number",
			"Gender",
			"T-shirt size",
			"Background",
			"University",
			"Study",
			"Work",
			"WWCC",
			"WWCC Number",
			"Curtin Status",
			"Curtin Associate/Staff ID",
			"Referral",
			"Coding Experience",
			"Child-Related Experience",
			"Coding Knowledge/Interest",
			"Experience with Young People",
			"Aim",
			"Confirmation")

		val = CSVValidator(fields)

		val.add_header_check('EX1', 'bad header')
		val.add_record_length_check('EX2', 'unexpected record length')
		status = val.validate(reader)
		csvfile.seek(0)
		if len(status) is 0:
			return True
		else:
			return False