from .views import ImageUploadView


def initialize_routes(api):
	"""
	"""
	api.add_resource(ImageUploadView, '/media/upload')
