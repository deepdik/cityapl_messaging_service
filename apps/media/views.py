import json

from flask import Blueprint
from flask import request, jsonify, abort
from flask_restful import Resource

from app import mongo, postgres
from .utils import S3FileUpload
from .validators import UploadFileToAWSSchema
	
from config.db_connect import PostgresExcecuteQuery
from config.credentials import AWS_PRODUCT_BUCKET
from flask import jsonify, make_response
from marshmallow import ValidationError
from utils import pylogger
from utils.decorators import authenticate
from utils import pylogger


# class Product(Resource):
# 	"""
# 	"""
# 	# method_decorators = [authenticate]
# 	# @cache.cached(timeout=50)
# 	def get(self, *args, **kwargs):
# 		"""
# 		"""
# 		data = list(mongo.db.product.find())
# 		return jsonify({'data': data})

class ImageUploadView(Resource):
	"""
	"""
	# method_decorators = [authenticate]

	def post(self, *args, **kwargs):
		"""
		Pending: Need to make file name unique
		"""
		data = request.form
		if not request.files.get('file'):
			return {'message': 'file required',}, 400
		schema = UploadFileToAWSSchema()
		try:
			validated_data = schema.load(data)
		except ValidationError as err:
			return err.messages, 400
		else:
			try:
				print(request.files['file'])
				filename = request.files['file'].filename
				# for product images
				if validated_data['file_type'] == '1':
					status = S3FileUpload.upload_to_aws(
						request.files['file'],
						AWS_PRODUCT_BUCKET,
						filename,
						extra_args = {
							'ContentType': "image/png",
							'ACL': "public-read"
							}
					)
					url = self.generate_file_url(AWS_PRODUCT_BUCKET, filename)
				if status:
					return {'message': 'uploaded successfully',
							'url': url}, 200
				else:
					pylogger.logger.error(e)
					abort(500)
			except Exception as e:
				print(e)
				pylogger.logger.error(e)
				abort(500)

	def generate_file_url(self, bucket_name, filename):
		"""
		http://s3-REGION-.amazonaws.com/BUCKET-NAME/KEY
		"""
		s3_domain = '%s.s3.amazonaws.com' % bucket_name
		s_media_url = 'https://%s/%s' % (s3_domain, filename)
		return s_media_url


class SendEmailView(Resource):
	"""
	"""
	def post(self, *args, **kwargs):
		"""
		"""
		data = request.json
		schema = SendEmailSchema()
		try:
			validated_data = schema.load(data)
		except ValidationError as err:
			return err.messages, 400
		else:
			try:
				status = AWSSendEmail(
					validated_data.get('send_to'),
					subject='check',
					body_html='check',
					body_text='',
					attachments=[],
				 	sender_mail='dk5f95@gmail.com',
					).send_mail()
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

