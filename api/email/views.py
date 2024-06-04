from api.email.tasks import send_email_task
from fastapi import APIRouter

from core.config import settings

router = APIRouter(tags=["Email"])


@router.get("/send-email-after-registration/")
async def send_email_after_registration():
    email_host = settings.email.host
    email_port = settings.email.port
    email_user = settings.email.user
    email_password = settings.email.password
    email_use_ssl = settings.email.use_ssl
    receiver_email = "pashattaguzov@yandex.ru"

    send_email_task.delay(
        email_user,
        email_password,
        email_host,
        email_port,
        email_use_ssl,
        receiver_email,
    )

    return {"message": "Email sending task queued"}
