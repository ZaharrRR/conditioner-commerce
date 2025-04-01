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

ENV NODE_ENV production
ENV NITRO_HOST 0.0.0.0
ENV NITRO_PORT 5000

COPY --from=builder /app/package*.json ./
COPY --from=builder /app/.output ./.output

RUN npm install --production

CMD ["node", ".output/server/index.mjs"]