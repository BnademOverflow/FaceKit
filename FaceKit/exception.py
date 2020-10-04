class CookiesInvalid(Exception):
	def __init__(self, session_number):
		super().__init__("cookies not valid in account number '{}'".format(session_number))

class ArgumentError(Exception):
	pass