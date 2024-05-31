from sqlalchemy.orm import Mapped

from core.models import Base


class User(Base):
    email: Mapped[str]
    password: Mapped[str]
