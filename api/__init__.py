from fastapi import APIRouter

from api.contacts import router as contacts_router
from api.resumes import router as resumes_router
from api.vacancies import router as vacancies_router
from api.email import router as emails_router
from core.config import settings

router = APIRouter(
    prefix=settings.api.prefix,
)
router.include_router(resumes_router)
router.include_router(contacts_router)
router.include_router(vacancies_router)
router.include_router(emails_router)
