from fastapi import APIRouter

from api.resumes import router as resumes_router
from core.config import settings


router = APIRouter(
    prefix=settings.api.prefix,
)
router.include_router(resumes_router)
