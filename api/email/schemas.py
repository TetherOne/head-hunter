from pydantic import BaseModel


class EmailSend(BaseModel):
    email: str
