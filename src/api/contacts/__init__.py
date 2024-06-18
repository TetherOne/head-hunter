from fastapi import APIRouter

from src.core.config import settings

from .views import router as contacts_router

router = APIRouter()

router.include_router(
    contacts_router,
    prefix=settings.api.contacts,
)
