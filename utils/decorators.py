import jwt
from functools import wraps
from flask import g, request, redirect, url_for
from flask_restful import abort


def authenticate(func):
	"""
	"""
	@wraps(func)
	def wrapper(*args, **kwargs):
		if not getattr(func, 'authenticated', True):
			return func(*args, **kwargs)

		# custom account lookup function
		access_token = request.headers.get('Authorization')
		print(access_token)

		# verify token
		# if acct:
		# 	return func(*args, **kwargs)

		abort(401)
	return wrapper


