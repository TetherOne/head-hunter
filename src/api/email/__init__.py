from fastapi import APIRouter

from src.core.config import settings

from .views import router as email_router

router = APIRouter()


router.include_router(
    email_router,
    prefix=settings.api.email,
)
