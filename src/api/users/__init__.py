from fastapi import APIRouter

from src.core.config import settings

from .views import router as users_router

router = APIRouter()

router.include_router(
    users_router,
    prefix=settings.api.users,
)
