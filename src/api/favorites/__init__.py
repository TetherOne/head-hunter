from fastapi import APIRouter

from src.core.config import settings

from .views import router as favorites_router

router = APIRouter()

router.include_router(
    favorites_router,
    prefix=settings.api.favorites,
)
