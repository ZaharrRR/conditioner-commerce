from fastapi import FastAPI

from api.v1.attribute import router as attribute_router
from api.v1.brand import router as brand_router
from core import logger, settings

app = FastAPI()

app.include_router(attribute_router)
app.include_router(brand_router)

if __name__ == "__main__":
    import uvicorn

    logger.info("FastAPI сервер запущен!")
    uvicorn.run(app, host=settings.api.host, port=settings.api.port)
