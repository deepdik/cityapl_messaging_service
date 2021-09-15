from .views import SendMessage


def initialize_routes(api):
	"""
	"""
	api.add_resource(SendMessage, '/send/sms')

