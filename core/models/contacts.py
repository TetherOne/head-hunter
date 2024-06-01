from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class Contact(Base):
    phone: Mapped[str]
    email: Mapped[str]
    telegram: Mapped[str] = mapped_column(nullable=True)
    linkedin: Mapped[str] = mapped_column(nullable=True)
    github: Mapped[str] = mapped_column(nullable=True)
    gitlab: Mapped[str] = mapped_column(nullable=True)
