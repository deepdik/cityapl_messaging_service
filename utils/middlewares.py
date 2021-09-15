import os
import logging

from werkzeug import Request, Response

from config import settings


AUDIT_LOG = os.path.join(settings.BASE_DIR, 'logs/requests.log')
LOG = logging.getLogger(__name__)
LOG.addHandler(logging.FileHandler(AUDIT_LOG))

class OperationLogMiddleware:
    """
    wsgi level logging
    """
    def __init__(self, app):
        self._app = app

    def __call__(self, environ, start_response):
        req = Request(environ)
        resp = Response(start_response)
        self._process_request(req)
        self._process_response(resp)
        return self._app(environ, start_response)

    @staticmethod
    def _process_request(request):
        with open(AUDIT_LOG, 'a+', encoding='UTF-8') as f:
            print(f'hello request: {request.method}', file=f)

    @staticmethod
    def _process_response(response):
        with open(AUDIT_LOG, 'a+', encoding='UTF-8') as f:
            print(f'hello response: {response.status_code}', file=f)
