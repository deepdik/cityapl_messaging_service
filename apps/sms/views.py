import json

from flask import Blueprint
from flask import request, jsonify, abort
from flask_restful import Resource

from app import mongo, postgres
from .utils import SendSMS
from .validators import SendMessageSchema
from config.db_connect import PostgresExcecuteQuery
from config.credentials import AWS_PRODUCT_BUCKET
from flask import jsonify, make_response
from marshmallow import ValidationError
from utils import pylogger
from utils.decorators import authenticate
from utils import pylogger


class SendMessage(Resource):
	"""
	"""
	def post(self, *args, **kwargs):
		"""
		"""
		data = request.json
		schema = SendMessageSchema()
		try:
			validated_data = schema.load(data)
		except ValidationError as err:
			return err.messages, 400
		else:
			try:
				status = SendSMS.fast2_sms_send(
					','.join(mobile_numbers),
					validated_data['message']
					)
				if status:
					return {'message': 'sent successfully',
							'url': url}, 200
				else:
					pylogger.logger.error(e)
					abort(500)
			except Exception as e:
				print(e)
				pylogger.logger.error(e)
				abort(500)

