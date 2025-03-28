from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    logger.info("Бот запущен")
    await start_bot()
    app.include_router(attribute_router)
    app.include_router(brand_router)
    app.include_router(category_router)
    app.include_router(product_router)
    app.include_router(order_router)
    app.include_router(service_router)
    yield
    logger.info("Бот остановлен")
    await stop_bot()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn

    logger.info("FastAPI сервер запущен!")
    uvicorn.run(app, host=settings.api.host, port=settings.api.port)
