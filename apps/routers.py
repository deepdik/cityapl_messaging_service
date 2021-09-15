from utils.utils import include_routers


def initialize_routes(api):
	"""
	Include all app routes
	"""
	include_routers('apps.media.routers', api)
	include_routers('apps.mail.routers', api)
	include_routers('apps.sms.routers', api)

