FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

ARG ENV=production
ENV ENV=${ENV}

EXPOSE 3000

CMD if [ "$ENV" = "development" ] ; then \
        cd src && alembic -c alembic.ini upgrade head && \
        uvicorn main:app --host 0.0.0.0 --port 3000 --reload ; \
    else \
        cd src && alembic -c alembic.ini upgrade head && \
        uvicorn main:app --host 0.0.0.0 --port 3000 ; \
    fi
