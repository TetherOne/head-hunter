from fastapi import APIRouter

from core.config import settings

from .views import router as auth_router

router = APIRouter()

router.include_router(
    auth_router,
    prefix=settings.api.auth,
)
