from apps.mail.views import  SendEmailView


def initialize_routes(api):
	"""
	"""
	api.add_resource(SendEmailView, '/send/email')