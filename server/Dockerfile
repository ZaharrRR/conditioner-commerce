FROM python:3.13-alpine

RUN apk add --no-cache \
    build-base \
    libffi-dev \
    postgresql-dev \
    netcat-openbsd

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .


CMD   cd src && alembic -c alembic.ini upgrade head && python main.py