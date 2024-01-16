from dotenv import dotenv_values
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import numpy as np
import cv2

config = dotenv_values(".env")


def mail_sender(receiver_email, name, phone, body, imgs=None):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = config['EMAIL']
    password = config['PASSWORD']

    subject = f"{name} {phone}'dan Yeni E-posta"
    body = body

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    for img in imgs:
        if img is not None:
            img_bytes = cv2.imencode(".jpg", img)[1].tobytes()
            part = MIMEBase("application", "octet-stream")
            part.set_payload(img_bytes)
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {name}_{phone}_photo.jpg",
            )
            message.attach(part)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
