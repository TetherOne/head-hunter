from fastapi import APIRouter

from core.config import settings

from .views import router as vacancies_router

router = APIRouter()

router.include_router(
    vacancies_router,
    prefix=settings.api.vacancies,
)
