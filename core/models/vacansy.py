from sqlalchemy.orm import Mapped

from core.models import Base


class Vacancy(Base):
    job_tittle: Mapped[str]
    description: Mapped[str]
    address: Mapped[str | None]
    phone: Mapped[str | None]
    email: Mapped[str | None]
