"""
"""
import datetime

from marshmallow import Schema, fields, ValidationError, validate
from marshmallow.validate import Range


class UploadFileToAWSSchema(Schema):
	"""
	Schema validate before Image upload

	1 - product images
	"""
	file_type = fields.String(validate=validate.OneOf(['1']), required=True)

