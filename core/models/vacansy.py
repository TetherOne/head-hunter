from sqlalchemy.orm import Mapped

from core.models import Base


class Vacancy(Base):
    job_tittle: Mapped[str]
    description: Mapped[str]
    experience: Mapped[str]
    salary: Mapped[int]
    address: Mapped[str | None]
    phone: Mapped[str | None]
    email: Mapped[str | None]
