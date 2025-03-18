# Шаг сборки
FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
COPY .npmrc* ./
COPY nuxt.config.ts ./

RUN npm install

COPY . .

RUN npm run build

# Финальный образ
FROM node:18-alpine

WORKDIR /app

# Копируем необходимые файлы
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/.output ./.output


CMD [ "npm", "run", "preview" ]