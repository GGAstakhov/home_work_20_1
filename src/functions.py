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
    msg['From'] = 'goha1115A23@yandex.ru'
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))

    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_MAIL, SMTP_PASSWORD)
            server.send_message(msg)
    except smtplib.SMTPServerDisconnected as e:
        print("SMTP server disconnected. Reconnecting...")
        server = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
        server.login(SMTP_MAIL, SMTP_PASSWORD)
        server.send_message(msg)


def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
