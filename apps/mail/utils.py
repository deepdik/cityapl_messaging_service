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


class AWSSendEmail:

    def __init__(self, recipient:list, subject='', body_html='', body_text='', attachments=[], sender_mail=None):
        """
        taking recipient = []  (only for attachment  mail)
        """
        self.client = AWSClientSingleton.get_client('ses')

        self.sender = sender_mail
        self.charset = "UTF-8"

        self.recipient = recipient
        self.subject = subject
        self.body_text = body_text
        self.body_html = body_html
        self.attachments = attachments

    def send_mail(self):
        """
        send plain email without attachment
        """
        # Try to send the email.
        try:
            response = self.client.send_email(
                Destination={
                    'ToAddresses': self.recipient
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': self.charset,
                            'Data': self.body_html,
                        },
                        'Text': {
                            'Charset': self.charset,
                            'Data': self.body_text,
                        },
                    },
                    'Subject': {
                        'Charset': self.charset,
                        'Data': self.subject,
                    },
                },
                Source=self.sender,
            )
        # Display error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
            pylogger.logger.error(e)
            pylogger.logger.error(e.response['Error']['Message'])
            return False
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])
            return True

    def send_attachment_mail(self):
        """
        send email with attachments
        taking recipient = []  (list for attachment mail)
        """
        msg = MIMEMultipart('mixed')
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = ', '.join(self.recipient)
        textpart = MIMEText(self.body_text.encode(self.charset), 'plain', self.charset)
        htmlpart = MIMEText(self.body_html.encode(self.charset), 'html', self.charset)

        msg_body = MIMEMultipart('alternative')
        msg_body.attach(textpart)
        msg_body.attach(htmlpart)
        msg.attach(msg_body)

        # image attachement in mail html
        # fp = open(os.path.abspath('logo.png'), 'rb')
        # image = MIMEImage(fp.read())
        # fp.close()
        # Specify the  ID according to the img src in the HTML part
        # image.add_header('Content-ID', '<logo>')
        # msg.attach(image)

        for attachment in self.attachments:
            att = MIMEApplication(open(attachment, 'rb').read())
            att.add_header(
                'Content-Disposition',
                'attachment',
                filename=os.path.basename(attachment)
            )
            msg.attach(att)

        try:
            response = self.client.send_raw_email(
                Source=self.sender,
                Destinations=self.recipient,
                RawMessage={'Data': msg.as_string(),},
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
            pylogger.logger.error(e)
            pylogger.logger.error(e.response['Error']['Message'])
            return False
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])
            return True

