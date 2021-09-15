"""
To use logging:
    from . import pylogging

    pylogging.logger.info("Test info")
    pylogging.logger.warnign("Test warnign")
    pylogging.logger.error("Test error")

    pylogging.logger_info_with_request(request, data)
    pylogging.logger_info(data)
"""
import os
import logging
from config import settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

log_path = os.path.join(settings.BASE_DIR, 'logs/project.log')

## create a file handler
handler = logging.FileHandler(log_path)
# handler.setLevel(logging.INFO)

## create a logging format
formatter = logging.Formatter('[%(asctime)-6s]:%(name)s - %(levelname)s - %(module)s - %(funcName)s -  %(lineno)d -%(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


def logger_info_with_request(request, data):
    if getattr(settings, 'PY_LOGGING', True):
        print(request.headers)
        user_agent = request.headers.get('User-Agent')
        content_type = request.headers.get('CONTENT_TYPE', '')

        log_msg = "{api} - {content_type} - {user_agent}\n {data}".format(
            api=request.path,
            content_type=content_type,
            user_agent=user_agent,
            data=data)
        logger.info(log_msg)
    else:
        pass

