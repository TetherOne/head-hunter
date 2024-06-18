from fastapi import APIRouter, status

from src.api.email.schemas import EmailSend
from src.api.email.tasks import send_email_task
from src.core.config import settings

router = APIRouter(tags=["Email"])


@router.post(
    "/send-email-after-registration/",
    status_code=status.HTTP_200_OK,
)
async def send_email_after_registration(
    email: EmailSend,
):
    email_host = settings.email.host
    email_port = settings.email.port
    email_user = settings.email.user
    email_password = settings.email.password
    email_use_ssl = settings.email.use_ssl

    send_email_task.delay(
        email_user,
        email_password,
        email_host,
        email_port,
        email_use_ssl,
        email.email,
    )
