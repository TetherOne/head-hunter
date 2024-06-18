from fastapi import APIRouter

from src.api.contacts import router as contacts_router
from src.api.email import router as emails_router
from src.api.favorites import router as favorites_router
from src.api.resumes import router as resumes_router
from src.api.users import router as users_router
from src.api.vacancies import router as vacancies_router
from src.core.config import settings

router = APIRouter(
    prefix=settings.api.prefix,
)
router.include_router(resumes_router)
router.include_router(contacts_router)
router.include_router(vacancies_router)
router.include_router(emails_router)
router.include_router(favorites_router)
router.include_router(users_router)
