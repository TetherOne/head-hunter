from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api import router
from core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    """
    Закрываем соединение после завершения
    работы приложения
    """
    await db_helper.dispose()


hh_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
hh_app.include_router(
    router,
)
