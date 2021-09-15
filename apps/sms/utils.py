import os
import zipfile

import logging
import boto3
from botocore.exceptions import ClientError
from config.credentials import (AWS_ACCESS_KEY_ID,
    AWS_SECRET_KEY, AWS_REGION, FAST2SMS_API)

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from utils import pylogger


class SendSMS:
    """
    """
    @staticmethod
    def fast2_sms_send(number, message):
        """
        """
        url = "https://www.fast2sms.com/dev/bulkV2"
        payload = "sender_id={}&message={}&route=v3&numbers={}".format(
            'CITYAPL',
            message,
            number
            )
        headers = {
            'authorization': FAST2SMS_API,
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        if response.status_code == 200:
            return True
        return False

