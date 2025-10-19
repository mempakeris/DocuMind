FROM golang:1.25.3-alpine AS build

WORKDIR /app

RUN apk add --no-cache git

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o worker .

FROM alpine:latest

WORKDIR /app

COPY --from=build /app/worker .