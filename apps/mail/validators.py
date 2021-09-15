"""
"""
import datetime

from marshmallow import Schema, fields, ValidationError, validate
from marshmallow.validate import Range


class SendEmailSchema(Schema):
	"""
	"""
	send_to = fields.List(fields.String(), required=True)

