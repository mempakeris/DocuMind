FROM node:25-alpine AS build

WORKDIR /app

RUN apk add --no-cache bash curl

# I guess sh causes issues here :thinking:
RUN curl -fsSL https://bun.sh/install | bash

ENV PATH="/root/.bun/bin:$PATH"

COPY bun.lock package.json ./

RUN bun install

COPY . .