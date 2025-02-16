from fastapi import FastAPI

from api.v1.attribute import router as attribute_router
from api.v1.brand import router as brand_router
from api.v1.category import router as category_router
from api.v1.product import router as product_router
from core import logger, settings

app = FastAPI()

app.include_router(attribute_router)
app.include_router(brand_router)
app.include_router(category_router)
app.include_router(product_router)

if __name__ == "__main__":
    import uvicorn

    logger.info("FastAPI сервер запущен!")
    uvicorn.run(app, host=settings.api.host, port=settings.api.port)
