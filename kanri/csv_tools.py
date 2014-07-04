from kanri import knowledge

def yes_no(text, fuzzy = False):
	if fuzzy:
		if 'Yes' in text:
			return True
		elif 'No' in text:
			return False
		elif text == '':
			return False
		else:
			raise ValueError("Yes or No cannot be parsed from value: %s" % text)
	else:
		if text == 'Yes':
			return True
		elif text == 'No':
			return False
		else:
			raise ValueError("Value is not Yes or No and cannot be parsed: %s" % text)

def knowledge_parse(text):
	if text == "I know nothing but am keen to learn!":
		return knowledge.NOTHING
	elif text == "I know some basics":
		return knowledge.BEGINNER
	elif text == "I know quite a lot":
		return knowledge.INTERMEDIARY
	elif text == "I know a great deal":
		return knowledge.ADVANCED
	else:
		raise ValueError("Not a valid knowledge choice: %s" % text)

def none_catch(text):
	if text == '':
		return None
	else:
		return text