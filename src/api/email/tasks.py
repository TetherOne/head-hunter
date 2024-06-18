import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.api.email.celery import celery


@celery.task
def send_email_task(
    email_user,
    email_password,
    email_host,
    email_port,
    email_use_ssl,
    receiver_email,
):
    sender_email = email_user
    subject = "Head Hunter Team"
    body = "Спасибо за то, что выбрали наш сервис!"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(
        MIMEText(
            body,
            "plain",
        ),
    )

    server = (
        smtplib.SMTP_SSL(
            email_host,
            email_port,
        )
        if email_use_ssl
        else smtplib.SMTP(
            email_host,
            email_port,
        )
    )
    server.login(
        email_user,
        email_password,
    )
    server.send_message(message)
    server.quit()
