import uuid

import bcrypt
from fastapi import HTTPException, status


async def check_password(qrcode_update, qrcode):
    """
    Проверка пароля
    """
    if qrcode_update.password:
        if not validate_password(
            qrcode_update.password,
            qrcode.password,
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid password",
            )


def hash_password(password: str) -> str:
    pwd_bytes = password.encode()
    return bcrypt.hashpw(
        pwd_bytes,
        bcrypt.gensalt(10),
    ).decode()


def validate_password(
    password: str,
    hashed_password: str,
) -> bool:
    return bcrypt.checkpw(
        password.encode(),
        hashed_password.encode(),
    )


def generate_token():
    return str(uuid.uuid4())
