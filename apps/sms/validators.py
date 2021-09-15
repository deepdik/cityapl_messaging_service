"""
"""
import datetime

from marshmallow import Schema, fields, ValidationError, validate
from marshmallow.validate import Range


class SendMessageSchema(Schema):
	"""
	"""
	message = fields.String(required=True)
	mobile_numbers = fields.List(fields.String(), required=True)
