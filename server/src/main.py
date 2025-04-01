from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from sqlalchemy.exc import DatabaseError
from pydantic import ValidationError
from api.v1.attribute import router as attribute_router
from api.v1.brand import router as brand_router
from api.v1.category import router as category_router
from api.v1.order import router as order_router
from api.v1.product import router as product_router
from api.v1.services import router as service_router
from bot.bot import start_bot, stop_bot


from core import logger, settings


origins = [
    "http://localhost",
    "http://localhost:5000",
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_bot()
    app.include_router(attribute_router)
    app.include_router(brand_router)
    app.include_router(category_router)
    app.include_router(product_router)
    app.include_router(order_router)
    app.include_router(service_router)

    yield
    await stop_bot()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ValidationError)
def handle_pydantic_validation_error(
        request: Request,
        exc: ValidationError,
) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "message": "Unhandled error",
            "error": exc.errors(),
        },
    )


@app.exception_handler(DatabaseError)
def handle_db_error(
        request: Request,
        exc: ValidationError,
) -> ORJSONResponse:
    logger.error(
        "Unhandled database error",
        exc_info=exc,
    )
    return ORJSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": "An unexpected error has occurred. "
                       "Our admins are already working on it."
        },
    )

if __name__ == "__main__":
    import uvicorn

    logger.info("FastAPI сервер запущен!")
    uvicorn.run(app, host=settings.api.host, port=settings.api.port)
