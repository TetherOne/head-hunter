from fastapi import APIRouter

from core.config import settings

from .views import router as resumes_router


router = APIRouter()

router.include_router(
    resumes_router,
    prefix=settings.api.resumes,
)
