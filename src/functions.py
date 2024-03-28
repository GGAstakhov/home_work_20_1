import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string

SMTP_HOST = os.environ.get('smtp_ya_host')
SMTP_MAIL = os.environ.get('smtp_ya_mail')
SMTP_PASSWORD = os.environ.get('smtp_ya_password')
SMTP_PORT = (os.environ.get('smtp_ya_port'))


def send_mail(to_addr, subject, text):

    msg = MIMEMultipart()
    msg['From'] = 'new.gres@yandex.ru'
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_MAIL, SMTP_PASSWORD)
        server.send_message(msg)


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
