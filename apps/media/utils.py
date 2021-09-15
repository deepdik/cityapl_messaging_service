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


class AWSClientSingleton:
    """
    Singleton class to create AWS client
    """
    __SES_instance = None
    __S3_instance = None

    @classmethod
    def get_client(cls, service):
        """ 
        static method to get instance
        """
        if service == 's3':
            if not cls.__S3_instance:
                cls.__S3_instance = cls.__create_client(service)
            return cls.__S3_instance

        elif service == 'ses':
            if not cls.__SES_instance:
                cls.__SES_instance = cls.__create_client(service)
            return cls.__SES_instance
        else:
            return None

    @staticmethod
    def __create_client(service):
        """
        """
        client = boto3.client(
            service,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=AWS_REGION
        )
        return client


class S3FileUpload:
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    def upload_to_aws(local_file, bucket, s3_file, extra_args={}):
        """
        """
        s3 = AWSClientSingleton.get_client('s3')
        try:
            s3.upload_fileobj(
                local_file,
                bucket,
                s3_file,
                ExtraArgs=extra_args
                )
            return True
        except Exception as e:
            print(e)
            pylogger.logger.error(e)
            return False

