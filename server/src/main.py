from fastapi import FastAPI

from core import settings

app = FastAPI()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT)
